from ..scene import Scene
from subprocess import run
from pathlib import Path

def render(scene: Scene, output: Path, fps, keep_frames: bool):
    try:
        # ffmpeg -framerate {fps} -i {path} -c:v libx264 -pix_fmt yuv420p -y {output}
        video = run(
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
                str(output / f"{scene.width}x{scene.height}-{fps}.mp4")
            ], check=True, capture_output=True, text=True
        )
        if scene.audio_channels:
            # ffmpeg -i video.mp4 -i audio.mp3 -c:v copy -c:a aac -map 0:v:0 -map 1:a:0 -y output.mp4
            for channel in scene.audio_channels:
                for audio in channel:
                    video = run(
                        [
                            "ffmpeg",
                            "-i",
                            str(output / f"{scene.width}x{scene.height}-{fps}.mp4"),
                            "-i",
                            str(audio.path),
                            "-c:v",
                            "aac",
                            "-map",
                            "0:v:0",
                            "-map",
                            "1:v:0",
                            "-y",
                            str(output / f"{scene.width}x{scene.height}-{fps}.mp4")
                        ], check=True, capture_output=True, text=True
                    )
    except Exception:
        if not keep_frames:
            for frame in output.glob("frame*.png"):
                frame.unlink()
        
        raise RuntimeError(f"FFmpeg don't worked: {video.stdout}")