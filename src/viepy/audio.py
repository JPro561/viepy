from typing import Union, Optional
from pydub import AudioSegment
from pathlib import Path
from dataclasses import dataclass, field
from .Exceptions import AudioError
from shutil import which

@dataclass
class Audio:
    path: Union[str, Path] = None
    name: str = "Music"
    auto_play: bool = False
    _playing: bool = False
    duration: Optional[float] = None

    @property
    def playing(self):
        return self._playing

    def __post_init__(self):
        if which("ffprobe") is None:
            raise AudioError(
                "FFprobe was not found. Please install FFmpeg and add it to your PATH."
            )
        
        self.path = Path(self.path)

        if not self.duration:
            self.duration = len(AudioSegment.from_file(self.path)) / 1000

    def Play(self):
        if not self.playing:
            self.playing = True
        else:
            raise AudioError("The music is playing. It is impossible to play again the same Audio.")
    
    def Stop(self):
        if self.playing:
            self.playing = False
        else:
            raise AudioError("The music isn't playing. It is impossible to stop an audio that isn't playing.")

@dataclass
class Music(Audio):
    artist: str = "John Doe"
    album: Optional[str] = field(default=None, init=False)

@dataclass
class Sound_Effect(Audio):
    type: Optional[str] = None
