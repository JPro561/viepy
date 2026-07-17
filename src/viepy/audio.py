from typing import Union, Optional
from pydub import AudioSegment
import pathlib
from dataclasses import dataclass, field

@dataclass
class Audio:
    path: Union[str, pathlib.Path] = None
    name: str = "Music"
    auto_play: bool = False
    playing: bool = False
    duration: Optional[float] = None

    def __post_init__(self):
        if not self.duration:
            self.duration = len(AudioSegment.from_file(self.path)) / 1000

    def Play(self):
        if not self.playing:
            self.playing = True
        else:
            raise Exception("The music is playing. It is impossible to play again the same Audio.")
    
    def Stop(self):
        if self.playing:
            self.playing = False
        else:
            raise Exception("The music isn't playing. It is impossible to stop an audio that isn't playing.")

@dataclass
class Music(Audio):
    artist: str = "John Doe"
    album: Optional[str] = field(default=None, init=False)

@dataclass
class Sound_Effect(Audio):
    type: Optional[str] = None
