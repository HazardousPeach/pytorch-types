import torch


def is_available() -> bool: ...


def set_device(gpu: int) -> None: ...


class LongTensor(torch.LongTensor):
    ...


class FloatTensor(torch.FloatTensor):
    def __init__(self, k: int, val: float) -> None: ...
    ...


class ByteTensor(torch.ByteTensor):
    ...
