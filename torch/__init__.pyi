from typing import Any, Dict, List, Iterator, Union, Tuple, BinaryIO, overload, Sequence

class Tensor:
    data = ... # type: Any
    def __init__(self, arr : Any) -> None : ...
    def __getitem__(self, indices : Union[int, slice, Tuple[Union[slice, int], ...]]) \
        -> Any : ...
    def __add__(self, other : Union[float, 'Tensor']) -> 'Tensor' : ...
    def __radd__(self, other : float) -> 'Tensor' : ...
    def __mul__(self, other : Union[float, 'Tensor']) -> 'Tensor' : ...
    def __rmul__(self, other : float) -> 'Tensor' : ...
    def __truediv__(self, other : float) -> 'Tensor' : ...
    def __iter__(self) -> Iterator[Any] : ...
    def __next__(self) -> Any: ...
    def expand_as(self, t : 'Tensor') -> 'Tensor' : ...
    def squeeze(self, dim : int=None) -> 'Tensor' : ...
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

class LongTensor(Tensor):
    # @overload
    # def __add__(self, other : Union[float, 'Tensor']) -> 'Tensor' : ...
    # @overload
    # def __add__(self, other : Union[int, 'LongTensor']) -> 'LongTensor' : ...
    # @overload
    def __mod__(self, other : Union[int, 'LongTensor']) -> 'LongTensor' : ...
    def __rmod__(self, other : int) -> 'LongTensor' : ...
    def squeeze(self, dim : int=None) -> 'LongTensor': ...
    def view(self, *sizes : Union[Tensor, int]) -> 'LongTensor' : ...
    def repeat(self, *sizes : int) -> 'LongTensor' : ...
    ...

class FloatTensor(Tensor):
    def __init__(self, *args : Any) -> None : ...
    def view(self, *sizes : Union[Tensor, int]) -> 'FloatTensor' : ...
    def topk(self, k : int) -> Tuple['FloatTensor', 'LongTensor'] : ...
    def repeat(self, *sizes : int) -> 'FloatTensor' : ...
    def index_select(self, dim : int, index : 'LongTensor') -> 'FloatTensor' : ...
    ...

def zeros(*sizes : int) -> Tensor : ...
def save(data : Any, filehandle: BinaryIO) -> None : ...
def load(filename : str) -> Any : ...
def transpose(input : Tensor, dim0 : int, dim1 : int) -> Any : ...
@overload
def cat(tensors : Sequence[LongTensor], dim : int = 0) -> LongTensor : ...
@overload
def cat(tensors : Sequence[Tensor], dim : int = 0) -> Tensor : ...
