from torch import Tensor
from torch.utils.data.dataset import Dataset
from typing import Iterator, Tuple, List

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
      def __iter__(self) -> Iterator[Tuple[Tensor, Tensor]]: ...