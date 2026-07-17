import typing
from dataclasses import dataclass, field, InitVar
from .object import Object
from .audio import Music

from enum import Enum

class TextStyle(Enum):
    BOLD = "bold"
    ITALIC = "italic"
    UNDERLINE = "underline"
    STRIKETHROUGH = "through"

@dataclass
class Text(Object):
    text: str = "Hello Viepy!"
    style: typing.List[TextStyle] = field(default_factory=list)

    def replace_style(self, style: typing.List[str | TextStyle]):
        self.style = [
            s if isinstance(s, TextStyle) else TextStyle(s)
            for s in style
        ]
    
    def add_style(self, style: str | TextStyle):
        if isinstance(style, str):
            style = TextStyle(style)
        
        if style not in self.style:
            self.style.append(style)

        return self
    
    def remove_style(self, style: str | TextStyle):
        if isinstance(style, str):
            style = TextStyle(style)

        if style in self.style:
            self.style.remove(style)

        return self
    
    def clear_style(self):
        self.style.clear()

        return self

@dataclass
class Artist(Text):
    music: InitVar[Music] = None

    def __post_init__(self, music: Music):
        if music is not None:
            self.text = music.artist
        else:
            raise ValueError("Music not specified in the Artist() text class.")

@dataclass
class Music_Name(Text):
    music: InitVar[Music] = None

    def __post_init__(self, music: Music):
        if music is not None:
            self.text = getattr(music, 'title', getattr(music, 'name', 'Unknown Title'))
        elif music is None:
            raise ValueError("Music not specified in the Music_Name() text class.")
