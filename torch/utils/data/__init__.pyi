from torch import Tensor
from typing import Iterator, Sequence, overload


class Dataset:
    ...


class TensorDataset(Dataset):
    def __init__(self, *data: Tensor) -> None: ...
    ...


class DataLoader(Sequence[Sequence[Tensor]]):
    def __init__(self, dataset: Dataset,
                 batch_size: int = ...,
                 shuffle: bool = ...,
                 pin_memory: bool = ...,
                 num_workers: int = ...,
                 drop_last: bool = ...) -> None: ...

    def __iter__(self) -> Iterator[Sequence[Tensor]]: ...

    def __len__(self) -> int: ...

    @overload
    def __getitem__(self, i: int) -> Sequence[Tensor]: ...

    @overload
    def __getitem__(self, s: slice) -> Sequence[Sequence[Tensor]]: ...
