#!/usr/bin/env python3

import torch.optim

class LRScheduler:
    def __init__(self, optimizer: torch.optim.Optimizer) -> None:
        ...
    def step(self) -> None:
        ...

class StepLR(LRScheduler):
    def __init__(self, optimizer : torch.optim.Optimizer, step : int,
                 gamma : float = ...) -> None:
        ...
