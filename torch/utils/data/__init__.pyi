from torch import Tensor
from typing import Iterator, Tuple, List, Sequence

class Dataset:
      ...
class TensorDataset(Dataset):
      def __init__(self, *data : Tensor) -> None: ...
      ...

class DataLoader:
      def __init__(self, dataset : Dataset,
                   batch_size : int = ...,
                   shuffle : bool = ...,
                   pin_memory : bool = ...,
                   num_workers : int = ...,
                   drop_last : bool = ...) -> None: ...
      def __iter__(self) -> Iterator[Sequence[Tensor]]: ...
      def __len__(self) -> int: ...
