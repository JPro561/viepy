from typing import List
from dataclasses import dataclass, field
from .objects import Object
from .audio import Audio
from .text import FontManager
from .Exceptions import VariableError

@dataclass
class Scene:
    name: str = ""
    width: int = 1280
    height: int = 720
    fps: int = 60
    anti_aliasing: bool = True
    _objects: List[List[Object]] = field(default_factory=list)
    _audio_channels: List[List[Audio]] = field(default_factory=list)
    final_delay: float | None = None
    duration: float | None = None
    font_manager: FontManager = field(default_factory=FontManager)

    def add(self, *obj: Object):
        for o in obj:
            if o.z_index < 0:
                raise VariableError(
                    "z_index cannot be negative."
                )

            while len(self._objects) <= o.z_index:
                self._objects.append([])

            self._objects[o.z_index].append(o)

    def remove(self, obj: Object):
        if obj.z_index >= len(self._objects):
            raise VariableError("Object z_index does not exist.")

        try:
            self._objects[obj.z_index].remove(obj)
        except ValueError:
            raise VariableError("Object is not in this scene.")
    
    def clear(self):
        self._objects.clear()

    def add_audio_to_channel(self, audio: Audio, channel):
        while len(self._audio_channels) <= channel:
            self._audio_channels.append([])

        self._audio_channels[channel].append(audio)
    
    @property
    def objects(self):
        return tuple(tuple(layer) for layer in self._objects)
    
    @property
    def audio_channels(self):
        return list(list(channel) for channel in self._audio_channels)
