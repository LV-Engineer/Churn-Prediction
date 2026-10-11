import copy

import numpy as np
import torch
from scipy.sparse import issparse
from torch import nn
from torch.utils.data import DataLoader, TensorDataset

class MLP(nn.Module):
    def __init__(self, n_features: int, hidden=(64, 32), dropout: float = 0.3):
        super().__init__()
        layers, prev = [], n_features
        for h in hidden:
            layers += [nn.Linear(prev, h), nn.ReLU(), nn.Dropout(dropout)]
            prev = h
        layers.append(nn.Linear(prev, 1))
        self.net = nn.Sequential(*layers)

    def forward(self, x):
        return self.net(x).squeeze(1)

def to_tensor(X) -> torch.Tensor:
    X = X.toarray() if issparse(X) else np.asarray(X)
    return torch.tensor(X, dtype=torch.float32)

def train_mlp(X_train, y_train, X_val, y_val, *, seed, max_epochs=200, patience=15,
              lr=1e-3, weight_decay=1e-4, batch_size=128, hidden=(64, 32), dropout=0.3):
    torch.manual_seed(seed)
    Xt, Xv = to_tensor(X_train), to_tensor(X_val)
    yt = torch.tensor(np.asarray(y_train), dtype=torch.float32)
    yv = torch.tensor(np.asarray(y_val), dtype=torch.float32)

    model = MLP(Xt.shape[1], hidden, dropout)
    loss_fn = nn.BCEWithLogitsLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=lr, weight_decay=weight_decay)
    loader = DataLoader(TensorDataset(Xt, yt), batch_size=batch_size, shuffle=True,
                        generator=torch.Generator().manual_seed(seed))

    best_loss, best_epoch, wait = float("inf"), 0, 0
    best_state = copy.deepcopy(model.state_dict())

    for epoch in range(max_epochs):
        model.train()
        for xb, yb in loader:
            optimizer.zero_grad()
            loss_fn(model(xb), yb).backward()
            optimizer.step()

        model.eval()
        with torch.no_grad():
            val_loss = loss_fn(model(Xv), yv).item()
        if val_loss < best_loss:
            best_loss, best_state, best_epoch, wait = val_loss, copy.deepcopy(model.state_dict()), epoch, 0
        else:
            wait += 1
            if wait >= patience:
                break

    model.load_state_dict(best_state)
    return model, best_epoch

def predict_proba(model, X) -> np.ndarray:
    model.eval()
    with torch.no_grad():
        return torch.sigmoid(model(to_tensor(X))).numpy()