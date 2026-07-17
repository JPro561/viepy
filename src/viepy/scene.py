import typing
from dataclasses import dataclass, field
from .object import Object
from .audio import Audio

@dataclass
class Scene:
    width: int = 1280
    height: int = 720
    fps: int = 60
    anti_aliasing: bool = True
    objects: typing.List[Object] = field(default_factory=list)
    audio_channels: typing.List[typing.List[Audio]] = field(default_factory=list)
    final_delay: float | None = None
    duration: float | None = None

    def create_channel(self, channel: int):
        while len(self.audio_channels) <= channel:
            self.audio_channels.append([])
        
        return self.audio_channels

    def add_audio_to_channel(self, audio: Audio, channel):
        while len(self.audio_channels) <= channel:
            self.audio_channels.append([])

        self.audio_channels[channel].append(audio)
