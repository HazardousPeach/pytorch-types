
from typing import Dict, Any, List, Iterable

class Optimizer:
    def __init__(self, params : Iterable[Any], lr : float = ...) -> None: ...
    def zero_grad(self) -> None: ...
    def step(self) -> None: ...
    param_groups = ... # type: List[Dict[str, Any]]

class SGD(Optimizer):
    pass

class Adam(Optimizer):
    pass
