from pathlib import Path
from subprocess import run, CalledProcessError
from ...scene import Scene
from ...Exceptions import RenderError

def ffmpeg(scene: Scene, output: Path, fps: int, keep: bool):
    audio_files = [
        audio.path
        for channel in scene.audio_channels
        for audio in channel
    ]

    video_temp = output / "temp_video.mp4"
    audio_temp = output / "temp_audio.m4a"
    video_final = output / f"{scene.width}x{scene.height}-{fps}.mp4"

    try:
        run(
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
                str(video_temp if audio_files else video_final),
            ],
            check=True,
        )

        if audio_files:
            if not len(audio_files) == 1:
                cmd = ["ffmpeg"]

                for audio in audio_files:
                    cmd.extend([
                        "-i",
                        str(audio),
                    ])

                inputs = "".join(
                    f"[{i}:a]"
                    for i in range(len(audio_files))
                )

                cmd.extend([
                    "-filter_complex",
                    f"{inputs}concat=n={len(audio_files)}:v=0:a=1[outa]",
                    "-map",
                    "[outa]",
                    "-c:a",
                    "aac",
                    "-y",
                    str(audio_temp),
                ])

                run(cmd, check=True)

            if not len(audio_files) == 1:
                run(
                    [
                        "ffmpeg",
                        "-i",
                        str(video_temp),
                        "-i",
                        str(audio_temp),
                        "-map",
                        "0:v:0",
                        "-map",
                        "1:a:0",
                        "-c:v",
                        "copy",
                        "-c:a",
                        "aac",
                        "-shortest",
                        "-y",
                        str(video_final),
                    ],
                    check=True,
                )
            else:
                run(
                    [
                        "ffmpeg",
                        "-i",
                        str(video_temp),
                        "-i",
                        str(audio_files[0]),
                        "-map",
                        "0:v:0",
                        "-map",
                        "1:a:0",
                        "-c:v",
                        "copy",
                        "-c:a",
                        "aac",
                        "-shortest",
                        "-y",
                        str(video_final),
                    ],
                    check=True,
                )

        if not keep:
            for frame in output.glob("frame*.png"):
                frame.unlink()

            video_temp.unlink(missing_ok=True)
            audio_temp.unlink(missing_ok=True)

    except CalledProcessError as e:
        raise RenderError(
            "FFmpeg failed while rendering the video."
        ) from e

    except Exception as e:
        raise RenderError(
            f"Unexpected error while rendering video: {e}"
        ) from e

    return video_final
