import skia
import subprocess
from numpy import ceil
from pathlib import Path
from ..scene import Scene
from ..object import Circle, Triangle, Rectangle
import shutil

colors = {
    "red": skia.ColorRED,
    "blue": skia.ColorBLUE,
    "green": skia.ColorGREEN,
    "white": skia.ColorWHITE,
    "black": skia.ColorBLACK,
}

def render(scene: Scene, keep_frames: bool):
    # Checar ffmpeg
    if shutil.which("ffmpeg") is None:
        raise RuntimeError(
            "FFmpeg was not found. To run viepy, please install FFmpeg and add it in your PATH."
            "More informations in viepy Docs."
        )
    
    # Setando variaveis úteis
    scene_width, scene_height = scene.width, scene.height
    objects = scene.objects
    anti_aliasing = scene.anti_aliasing
    duration = scene.duration
    fps = scene.fps
    final_delay = 0 if scene.final_delay is None else scene.final_delay

    output = Path(f"viepy/videos/{scene.width}x{scene.height}/")

    output.mkdir(
        parents=True,
        exist_ok=True
    )

    if (duration is None) and (not scene.music_channels or not scene.music_channels[0]):
        raise ValueError("Scene has no duration. Specify duration or add a Music to channel 0.")
    else:
        if duration is None:
            duration = max(
                audio.duration
                for audio in scene.music_channels[0]
            )
    
    frames = ceil((duration + final_delay) * fps)
    
    # Render real
    for frame in range(frames):
        current_time = frame / fps

        surface = skia.Surface(scene_width, scene_height)
        canvas = surface.getCanvas()

        canvas.clear(skia.ColorWHITE)

        for obj in objects:
            paint = skia.Paint(
                Color=colors.get(
                    obj.color,
                    skia.ColorBLACK
                )
            )
            paint.setAntiAlias(anti_aliasing) 

            if isinstance(obj, Rectangle):
                rect = skia.Rect.MakeXYWH(
                    obj.x + scene_width / 2,
                    obj.y + scene_height / 2,
                    obj.width,
                    obj.height
                )
                canvas.drawRect(rect, paint)
            elif isinstance(obj, Circle):
                canvas.drawCircle(
                    obj.x + scene_width / 2,
                    obj.y + scene_height / 2,
                    obj.radius,
                    paint
                )
            else:
                raise Exception(f"The object '{obj}' isn't a valid object")

        image = surface.makeImageSnapshot()
        image.save(str(output / f"frame{frame:06d}.png"))
    
    try:
        video = subprocess.run(
            [
                "ffmpeg",
                "-framerate",
                str(fps),
                "-i",
                str(output / "frame%06d.png"),
                "-c:v",
                "libx264",
                "-pix_fmt",
                "yuv420p",
                "-y",
                str(output / f"{scene_width}x{scene_height}-{fps}.mp4")
            ], check=True, capture_output=True, text=True
        )
    except Exception:
        if not keep_frames:
            for frame in output.glob("frame*.png"):
                frame.unlink()
        
        raise RuntimeError(f"FFmpeg don't worked: {video.stdout}")
    
    if not keep_frames:
        for frame in output.glob("frame*.png"):
            frame.unlink()

    return output / f"{scene_width}x{scene_height}-{fps}.mp4"
