from dataclasses import dataclass, field
from typing import Tuple, Optional

@dataclass
class Object:
    """
    The origin class to all the objects.
    Example: obj = Object(x=0, y=0, rotate=90)
    """
    x: float = 0.0
    y: float = 0.0
    color: str = "blue"
    rotate: float = 0.0
    scale: Tuple[float, float] = (1.0, 1.0)

    react_property: Optional[str] = field(default=None, init=False)
    effect: Optional[str] = field(default=None, init=False)
    audio_channel: int = field(default=0, init=False)

    def apply_react(self, effect: str = "pulse", audio_channel: int = 0, property: str = "scale") -> None:
        """
        Binds an audio reaction effect to this object.
        Example: obj.apply_react(effect="pulse", audio_channel=1, property=scale)
        """
        self.effect = effect
        self.audio_channel = audio_channel
        self.react_property = property

@dataclass
class Rectangle(Object):
    width: float = 0.0
    height: float = 0.0


@dataclass
class Triangle(Object):
    size_1: float = 1.0
    size_2: float = 1.0
    size_3: float = 1.0

@dataclass
class Circle(Object):
    radius: float = 1.0
