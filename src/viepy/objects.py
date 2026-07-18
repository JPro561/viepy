from dataclasses import dataclass, field
from typing import Optional, List

@dataclass
class Transform:
    x: float = 0.0
    y: float = 0.0
    rotate: float = 0.0
    scale: List[float, float] = (1.0, 1.0)

@dataclass
class Object:
    """
    The origin class to all the objects.
    Example: obj = Object(x=0, y=0, rotate=90)
    """
    transform: Transform = field(default_factory=Transform(0, 0, 0, (1, 1)))
    z_index: int = 0
    color: str = "blue"
    visible: bool = True
    opacity: float = 1.0

    react_property: Optional[str] = field(default=None, init=False)
    effect: Optional[str] = field(default=None, init=False)
    audio_channel: int = field(default=0, init=False)

    def apply_react(
        self,
        effect: str = "pulse",
        audio_channel: int = 0,
        property: str = "scale"
    ) -> None:
        """
        Binds an audio reaction effect to this object.
        """
        self.effect = effect
        self.audio_channel = audio_channel
        self.react_property = property


@dataclass
class Rectangle(Object):
    width: float = 100.0
    height: float = 100.0


@dataclass
class Triangle(Object):
    size: float = 100.0
    
    @property
    def points(self):
        x = self.scale[0] / 2
        y = self.scale[1] / 2

        self.points = [
            (self.x, self.y - y),
            (self.x - x, self.y + y),
            (self.x + x, self.y + y)
        ]


@dataclass
class Circle(Object):
    radius: float = 50.0

@dataclass
class Group(Object):
    objects: List[Object] = field(default_factory=list)
