
from torch import Tensor
from typing import Tuple, Dict, Any

class GRU:
    def __init__(self, input_size : int, hidden_size : int) -> None : ...
    def __call__(self, input : Tensor, hidden : Tensor) \
        -> Tuple[Tensor, Tensor] : ...
    def cuda(self) -> 'GRU' : ...

class Embedding:
    def __init__(self, in_size : int, out_size : int) -> None : ...
    def __call__(self, input : Tensor) -> Tensor : ...
    def cuda(self) -> 'Embedding' : ...

class Linear:
    def __init__(self, hidden_size : int, output_size : int) -> None : ...
    def __call__(self, data : Tensor) -> Tensor : ...
    def cuda(self) -> 'Linear' : ...

class LogSoftmax:
    def __init__(self, dim : int) -> None : ...
    def __call__(self, data : Tensor) -> Tensor : ...
    def cuda(self) -> 'LogSoftmax' : ...

class Module:
    def cuda(self) -> 'Module': ...
    def __call__(self, *data : Tensor) -> Tensor: ...
    def parameters(self) -> Dict[str, Any] : ...
    def state_dict(self) -> Dict[str, Any] : ...
    def load_state_dict(self, state_dict : Dict[str, Any]) -> None : ...
    ...

class _Loss(Module): ...
class NLLLoss(_Loss): ...