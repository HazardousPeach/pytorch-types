
from torch import Tensor, FloatTensor, LongTensor
from typing import overload

@overload
def relu(t : FloatTensor) -> FloatTensor : ...
@overload
def relu(t : Tensor) -> Tensor : ...


def one_hot(t: LongTensor, num_classes: int) -> LongTensor: ...
