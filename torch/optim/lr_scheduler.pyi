#!/usr/bin/env python3

import torch.optim

class StepLR:
    def __init__(self, optimizer : torch.optim.Optimizer, step : int,
                 gamma : float = ...) -> None:
        ...
    def step(self) -> None:
        ...
