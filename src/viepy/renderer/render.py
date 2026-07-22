from .advanced.draw import draw
from .advanced.ffmpeg import ffmpeg
from numpy import ceil
from pathlib import Path
from ..scene import Scene
from shutil import which
from ..Exceptions import RenderError

def render(scene: Scene, keep: bool):
    if which("ffmpeg") is None or which("ffprobe") is None:
        raise RenderError(
            "FFmpeg was not found. To run viepy, please install FFmpeg and add it in your PATH."
            "More informations in viepy Docs."
        )
    
    fps = scene.fps
    final_delay = 0 if scene.final_delay is None else scene.final_delay

    output = Path(f".viepy/videos/{scene.name}/")

    output.mkdir(
        parents=True,
        exist_ok=True
    )

    if (scene.duration is None) and (not scene.audio_channels or not scene.audio_channels[0]):
        raise ValueError("Scene has no duration. Specify duration or add a Music to channel 0.")
    else:
        if scene.duration is None:
            scene.duration = max(
                audio.duration
                for audio in scene.audio_channels[0]
            )
    
    frames = int(ceil((scene.duration + final_delay) * fps))

    # render
    for frame in range(frames):
        current_time = frame / fps
        image = draw(scene, current_time)
        image.save(str(output / f"frame{frame:06d}.png"))
    
    # ffmpeg
    video = ffmpeg(scene, output, fps, keep)

    if not keep:
        for frame in output.glob("frame*.png"):
            frame.unlink()
        Path(output / "musics.txt").unlink(missing_ok=True)

    return video
