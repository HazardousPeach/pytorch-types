
from typing import Dict, Any, List

class Optimizer:
    pass

class SGD(Optimizer):
    def __init__(self, params : Dict[str, Any], lr : float = ...) -> None: ...
    def zero_grad(self) -> None: ...
    def step(self) -> None: ...
    param_groups = ... # type: List[Dict[str, Any]]
