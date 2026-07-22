from typing import List, Optional
from dataclasses import dataclass, field, InitVar
from .objects import Object
from .audio import Music
from skia import FontStyle
from enum import Enum
from subprocess import run
from pathlib import Path
from shutil import copy
from .Exceptions import TextError

class TextStyle(Enum):
    BOLD = "bold"
    ITALIC = "italic"
    UNDERLINE = "underline"
    STRIKETHROUGH = "through"

@dataclass
class Text(Object):
    text: str = "Hello Viepy!"
    style: List[TextStyle] = field(default_factory=list)
    font: Optional[str | Path] = None
    size: float = 24.0

    def replace_style(self, style: List[str | TextStyle]):
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
            raise TextError("Music not specified in the Artist() text class.")

@dataclass
class Music_Name(Text):
    music: InitVar[Music] = None

    def __post_init__(self, music: Music):
        if music is not None:
            self.text = getattr(music, 'title', getattr(music, 'name', 'Unknown Title'))
        elif music is None:
            raise TextError("Music not specified in the Music_Name() text class.")

class FontManager():
    def __init__(self):
        self.fonts_path = (
            Path(__file__).parent.parent
            / "viepy"
            / "assets"
            / "fonts"
        )

    def add_font(self, path_file: str):
        copy(path_file, self.fonts_path)
    
    def remove_font(self, font: str | Path):
        font = Path(font)

        if not font.is_absolute():
            font = self.fonts_path / font

        if not font.exists():
            raise TextError(
                f"Font does not exist: {font}"
            )

        font.unlink()
