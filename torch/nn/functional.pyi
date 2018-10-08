
from torch import Tensor, FloatTensor
from typing import overload

@overload
def relu(t : FloatTensor) -> FloatTensor : ...
@overload
def relu(t : Tensor) -> Tensor : ...
