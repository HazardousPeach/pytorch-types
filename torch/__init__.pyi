
from typing import (Any, List, Iterator, Union, Tuple, BinaryIO,
                    overload, Sequence, Optional, TypeVar)


class Tensor:
    data = ...  # type: Any
    def __init__(self, arr : Any) -> None : ...
    def __getitem__(self, indices : Union[int, slice, Tuple[Union[slice, int], ...]]) \
        -> Any: ...

    def __add__(self, other : Union[float, 'Tensor']) -> 'Tensor' : ...
    def add(self, float) -> 'Tensor' : ...
    def __radd__(self, other : float) -> 'Tensor' : ...
    def __mul__(self, other : Union[float, 'Tensor']) -> 'Tensor' : ...
    def __rmul__(self, other : float) -> 'Tensor' : ...
    def __truediv__(self, other : float) -> 'Tensor' : ...
    def __iter__(self) -> Iterator[Any] : ...
    def __next__(self) -> Any: ...
    def expand_as(self, t : 'Tensor') -> 'Tensor' : ...
    def expand(self, *sizes : int) -> 'Tensor' : ...
    def squeeze(self, dim : int=None) -> 'Tensor' : ...
    def unsqueeze(self, dim : int) -> 'Tensor' : ...
    def topk(self, k : int) -> Tuple['Tensor', 'LongTensor'] : ...
    def sort(self, dim : int = None, descending : bool = False) : ...
    def index_select(self, dim : int, index : 'LongTensor') -> 'Tensor' : ...
    def fill_(self, value : float) -> None : ...
    def index_fill_(self, dim : int, index : 'LongTensor' , value : float) \
        -> None : ...

    def cuda(self) -> 'Tensor': ...
    def view(self, *sizes : Union[Tensor, int]) -> 'Tensor' : ...
    def size(self, dim : int = None) -> 'Tensor' : ...
    def __len__(self) -> int : ...
    def backward(self) -> None : ...
    def repeat(self, *sizes : int) -> 'Tensor' : ...
    def item(self) -> Any: ...
    def contiguous(self) -> 'Tensor' : ...


T = TypeVar('T', bound=Tensor)


class ByteTensor(Tensor):
    def any(self) -> bool: ...
    def view(self, *sizes: Union[Tensor, int]) -> 'ByteTensor': ...
    def expand(self, *sizes: int) -> 'ByteTensor': ...


class LongTensor(Tensor):
    # @overload
    # def __add__(self, other : Union[float, 'Tensor']) -> 'Tensor' : ...
    # @overload
    # def __add__(self, other : Union[int, 'LongTensor']) -> 'LongTensor' : ...
    # @overload
    def add(self, float) -> 'LongTensor' : ...
    def __mod__(self, other : Union[int, 'LongTensor']) -> 'LongTensor' : ...
    def __rmod__(self, other : int) -> 'LongTensor' : ...
    def squeeze(self, dim : int=None) -> 'LongTensor': ...
    def unsqueeze(self, dim : int) -> 'LongTensor' : ...
    def expand_as(self, t : 'Tensor') -> 'LongTensor' : ...
    def expand(self, *sizes : int) -> 'LongTensor' : ...
    def view(self, *sizes : Union[Tensor, int]) -> 'LongTensor' : ...
    def repeat(self, *sizes : int) -> 'LongTensor' : ...
    def item(self) -> int: ...
    def contiguous(self) -> 'LongTensor' : ...
    def index_select(self, dim: int, index: 'LongTensor') -> 'LongTensor': ...
    def float(self) -> 'FloatTensor' : ...
    ...

class FloatTensor(Tensor):
    def __init__(self, *args : Any) -> None : ...
    def add(self, float) -> 'FloatTensor' : ...
    def view(self, *sizes : Union[Tensor, int]) -> 'FloatTensor' : ...
    def topk(self, k : int) -> Tuple['FloatTensor', 'LongTensor'] : ...
    def repeat(self, *sizes : int) -> 'FloatTensor' : ...
    def unsqueeze(self, dim : int) -> 'FloatTensor' : ...
    def expand_as(self, t : 'Tensor') -> 'FloatTensor' : ...
    def expand(self, *sizes : int) -> 'FloatTensor' : ...
    def index_select(self, dim : int, index : 'LongTensor') -> 'FloatTensor' : ...
    def item(self) -> float: ...
    def contiguous(self) -> 'FloatTensor' : ...
    ...


float32: int
float64: int
long: int
def zeros(*sizes : int, dtype : Optional[int] = None, **kwargs) -> Tensor : ...
def zeros_like(t : Tensor, dtype : Optional[int] = None) -> Tensor : ...
@overload
def save(data : Any, filehandle: BinaryIO, ) -> None : ...
@overload
def save(data : Any, filepath: str) -> None : ...
@overload
def load(f_handle : BinaryIO, map_location:Optional[str]=None) -> Any : ...
@overload
def load(filename : str, map_location:Optional[str]=None) -> Any : ...
def transpose(input : Tensor, dim0 : int, dim1 : int) -> Any : ...


def cat(tensors: Sequence[T], dim: int = 0) -> T: ...


def isnan(tensor: Tensor) -> ByteTensor: ...


def isinf(tensor: Tensor) -> ByteTensor: ...


def sum(tensor: Tensor) -> Tensor: ...


def manual_seed(n: int) -> None: ...


def where(mask: ByteTensor, t1: T, t2: T) -> T: ...


def stack(tensors: List[T]) -> T: ...
def full_like(tensor: T, value: Union[bool, int, float]) -> T: ...

class Size:
    def __init__(self, args: List[int]) -> None: ...
