from .advanced import draw, ffmpeg
from numpy import ceil
from pathlib import Path
from ..scene import Scene
from shutil import which
from ..Exceptions import RenderError

def render(scene: Scene, keep_frames: bool):
    if which("ffmpeg") is None:
        raise RenderError(
            "FFmpeg was not found. To run viepy, please install FFmpeg and add it in your PATH."
            "More informations in viepy Docs."
        )
    
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
        image = draw(scene)
        image.save(str(output / f"frame{frame:06d}.png"))
    
    # ffmpeg
    ffmpeg(scene, keep_frames)

    if not keep_frames:
        for frame in output.glob("frame*.png"):
            frame.unlink()

    return output / f"{scene.width}x{scene.height}-{fps}.mp4"
