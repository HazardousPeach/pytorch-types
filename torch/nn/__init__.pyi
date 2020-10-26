
from torch import Tensor, FloatTensor
from typing import Tuple, Dict, Any, overload, Iterable, TypeVar, Generic
from abc import ABCMeta, abstractmethod

ModuleType = TypeVar('ModuleType', bound='Module')

class Module(Generic[ModuleType], metaclass=ABCMeta):
    def cuda(self) -> ModuleType: ...
    def parameters(self) -> Iterable[Any] : ...
    def state_dict(self) -> Dict[Any, Any] : ...
    def load_state_dict(self, state_dict : Dict[str, Any]) -> None : ...
    def __call__(self, *args) -> Any : ...
    def add_module(self, name : str, model : Module) -> None: ...
    ...
class Linear(Module['Linear']):
    def __init__(self, hidden_size : int, output_size : int) -> None : ...
    def __call__(self, *args) -> Tensor : ...
class GRU(Module['GRU']):
    def __init__(self, input_size : int, hidden_size : int, num_layers : int = 1,
                 batch_first : bool = False) -> None : ...
    def __call__(self, *args) \
        -> Tuple[Tensor, Tensor] : ...

class Embedding(Module['Embedding']):
    def __init__(self, in_size : int, out_size : int) -> None : ...
    def __call__(self, *args) -> Tensor : ...
    def cuda(self) -> 'Embedding' : ...

class LogSoftmax(Module['LogSoftmax']):
    def __init__(self, dim : int) -> None : ...
    def __call__(self, *args) -> FloatTensor : ...
    def cuda(self) -> 'LogSoftmax' : ...


class _Loss(Module): ...
class NLLLoss(_Loss): ...
class MSELoss(_Loss): ...
