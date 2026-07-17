from typing import List, Optional
from dataclasses import dataclass, field, InitVar
from .objects import Object
from .audio import Music
from skia import FontStyle
from enum import Enum
from subprocess import run
from pathlib import Path

class TextStyle(Enum):
    BOLD = "bold"
    ITALIC = "italic"
    UNDERLINE = "underline"
    STRIKETHROUGH = "through"

@dataclass
class Text(Object):
    text: str = "Hello Viepy!"
    style: List[TextStyle] = field(default_factory=list)
    font: Optional[FontStyle] = None

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
    
    def add_font(self, path_file: str):
        run([
            "cp",
            str(path_file),
            str(Path("./assets/fonts/"))
        ])
    
    def remove_font_ttf(self, font):
        fonts = Path("./assets/fonts/")
        i = 0
        for f in fonts.glob('*.ttf'):
            if f == font:
                run([
                    "rm",
                    f"{fonts}/{f}"
                ])
                break
            i += 1

    def remove_font_otf(self, font):
        fonts = Path("./assets/fonts/")
        i = 0
        for f in fonts.glob('*.otf'):
            if f == font:
                run([
                    "rm",
                    f"{fonts}/{f}"
                ])
                break
            i += 1

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
