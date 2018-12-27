from typing import Any, Dict, List, Iterator, Union, Tuple, BinaryIO, overload, Sequence, Optional

class Tensor:
    data = ... # type: Any
    def __init__(self, arr : Any) -> None : ...
    def __getitem__(self, indices : Union[int, slice, Tuple[Union[slice, int], ...]]) \
        -> Any : ...
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
    def expand(self, *sizes : int) -> 'Tensor' : ...
    def view(self, *sizes : Union[Tensor, int]) -> 'LongTensor' : ...
    def repeat(self, *sizes : int) -> 'LongTensor' : ...
    def item(self) -> int: ...
    def contiguous(self) -> 'LongTensor' : ...
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

float32 : int
float64 : int
long : int
def zeros(*sizes : int, dtype : Optional[int] = None) -> Tensor : ...
def zeros_like(t : Tensor, dtype : Optional[int] = None) -> Tensor : ...
def save(data : Any, filehandle: BinaryIO) -> None : ...
@overload
def load(f_handle : BinaryIO) -> Any : ...
@overload
def load(filename : str) -> Any : ...
def transpose(input : Tensor, dim0 : int, dim1 : int) -> Any : ...
@overload
def cat(tensors : Sequence[LongTensor], dim : int = 0) -> LongTensor : ...
@overload
def cat(tensors : Sequence[FloatTensor], dim : int = 0) -> FloatTensor : ...
@overload
def cat(tensors : Sequence[Tensor], dim : int = 0) -> Tensor : ...
