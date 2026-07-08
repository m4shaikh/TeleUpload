from pathlib import Path
import re
import json
import subprocess

VIDEO_EXTENSIONS = {
    ".mp4",
    ".mkv",
    ".avi",
    ".mov",
    ".webm",
}


def get_video_files(folder):
    folder = Path(folder)

    files = [
        file
        for file in folder.iterdir()
        if file.is_file() and file.suffix.lower() in VIDEO_EXTENSIONS
    ]

    def extract_number(file):
        match = re.match(r"(\d+)", file.stem)
        return int(match.group(1)) if match else float("inf")

    files.sort(key=extract_number)

    return files


def get_video_metadata(video):
    """
    Extract duration, width and height using ffprobe.
    """

    result = subprocess.run(
        [
            "ffprobe",
            "-v", "quiet",
            "-print_format", "json",
            "-show_streams",
            str(video),
        ],
        capture_output=True,
        text=True,
        check=True,
    )

    data = json.loads(result.stdout)

    video_stream = next(
        stream
        for stream in data["streams"]
        if stream["codec_type"] == "video"
    )

    return {
        "duration": int(float(video_stream.get("duration", 0))),
        "width": video_stream.get("width", 0),
        "height": video_stream.get("height", 0),
    }


def generate_thumbnail(video, timestamp="5"):
    """
    Generate a thumbnail using ffmpeg.
    Returns the thumbnail path.
    """

    thumbnail = Path(video).with_suffix(".jpg")

    subprocess.run(
        [
            "ffmpeg",
            "-y",
            "-ss", timestamp,
            "-i", str(video),
            "-frames:v", "1",
            "-q:v", "2",
            str(thumbnail),
        ],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        check=True,
    )

    return thumbnail


def delete_thumbnail(thumbnail):
    """
    Delete the generated thumbnail.
    """

    Path(thumbnail).unlink(missing_ok=True)