# Copyright 2026 Cleverton Costa Santiago Júnior
# Licensed under the Apache License, Version 2.0 (the "License");
# 
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#     https://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# 
# See the License for the specific language governing permissions and
# limitations under the License.

from .draw import draw
from numpy import ceil
from pathlib import Path
from ..scene import Scene
import shutil

def render(scene: Scene, keep_frames: bool):
    # Checar ffmpeg
    if shutil.which("ffmpeg") is None:
        raise RuntimeError(
            "FFmpeg was not found. To run viepy, please install FFmpeg and add it in your PATH."
            "More informations in viepy Docs."
        )
    
    # Setando variaveis úteis
    fps = scene.fps
    final_delay = 0 if scene.final_delay is None else scene.final_delay

    output = Path(f"viepy/videos/{scene.width}x{scene.height}/")

    output.mkdir(
        parents=True,
        exist_ok=True
    )

    if (scene.duration is None) and (not scene.music_channels or not scene.music_channels[0]):
        raise ValueError("Scene has no duration. Specify duration or add a Music to channel 0.")
    else:
        if scene.duration is None:
            scene.duration = max(
                audio.duration
                for audio in scene.music_channels[0]
            )
    
    frames = ceil((scene.duration + final_delay) * fps)

    # render
    for frame in range(frames):
        current_time = frame / fps
        image = draw()
        image.save(str(output / f"frame{frame:06d}.png"))
    
    # ffmpeg
    render(scene, keep_frames)

    if not keep_frames:
        for frame in output.glob("frame*.png"):
            frame.unlink()

    return output / f"{scene.width}x{scene.height}-{fps}.mp4"
