from typing import List
from dataclasses import dataclass, field
from .objects import Object
from .audio import Audio
from .text import FontManager
from .Exceptions import VariableError

@dataclass
class Scene:
    width: int = 1280
    height: int = 720
    fps: int = 60
    anti_aliasing: bool = True
    _objects: List[List[Object]] = field(default_factory=list)
    audio_channels: List[List[Audio]] = field(default_factory=list)
    final_delay: float | None = None
    duration: float | None = None
    font_manager: FontManager = field(default_factory=FontManager)

    def add(self, *obj: Object):
        for o in obj:
            while len(self._objects) <= o.z_index:
                self._objects.append([])

            self._objects[o.z_index].append(o)

    def remove(self, obj: Object):
        for o in self._objects[obj.z_index]:
            if o == obj:
                self._objects[obj.z_index].remove(o)
    
    def clear(self):
        self._objects = []

    def create_channel(self, channel: int):
        while len(self.audio_channels) <= channel:
            self.audio_channels.append([])
        
        return self.audio_channels

    def add_audio_to_channel(self, audio: Audio, channel):
        while len(self.audio_channels) <= channel:
            self.audio_channels.append([])

        self.audio_channels[channel].append(audio)
    
    @property
    def objects(self):
        return tuple(tuple(layer) for layer in self._objects)
    
    @property
    def audio_channels(self):
        return self.audio_channels

    @property
    def font_manager(self):
        return self.font_manager
