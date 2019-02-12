from torch import Tensor, FloatTensor, LongTensor
from typing import Any, Union, Tuple, Iterator, overload

@overload
def Variable(t : FloatTensor, requires_grad : bool = True) -> FloatTensor: ...
@overload
def Variable(t : LongTensor, requires_grad : bool = True) -> LongTensor: ...
@overload
def Variable(t : Tensor, requires_grad : bool = True) -> Tensor: ...

class detect_anomaly:
    def __enter__(self) -> None:
        ...
    def __exit__(self, type, value, traceback) -> None:
        ...

# class Variable:
#       data = ... # type: Tensor
#       def __init__(self, t : Tensor) -> None : ...
#       def size(self) -> Tensor : ...
#       def __getitem__(self, indices : Tuple[Union[slice, int], ...]) -> Any : ...
#       def __add__(self, other : int) -> Variable : ...
#       def __iter__(self) -> Iterator[Any] : ...
#       def __next__(self) -> Any: ...
#       def backward(self) -> None : ...
#       ...
