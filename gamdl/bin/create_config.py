import json
import os


def check_config_file():
    return os.path.exists("config.json")

def create_default_config():
    default_config = {
        "disable_music_video_skip": False,
        "save_cover": False,
        "overwrite": False,
        "synced_lyrics_only": False,
        "no_synced_lyrics": False,
        "log_level": "INFO",
        "print_exceptions": False,
        "cookies_path": "cookies.txt",
        "language": "en-US",
        "output_path": "Apple Music",
        "temp_path": "temp",
        "wvd_path": None,
        "nm3u8dlre_path": "nm3u8dlre",
        "mp4decrypt_path": "mp4decrypt",
        "ffmpeg_path": "ffmpeg",
        "mp4box_path": "MP4Box",
        "download_mode": "nm3u8dlre",
        "remux_mode": "mp4box",
        "cover_format": "jpg",
        "template_folder_album": "{album_artist}/{album}",
        "template_folder_compilation": "Compilations/{album}",
        "template_file_single_disc": "{track:02d} {title}",
        "template_file_multi_disc": "{disc}-{track:02d} {title}",
        "template_folder_no_album": "{artist}/Unknown Album",
        "template_file_no_album": "{title}",
        "template_date": "%Y-%m-%dT%H:%M:%SZ",
        "exclude_tags": None,
        "cover_size": 1200,
        "truncate": 40,
        "codec_song": "aac-legacy",
        "synced_lyrics_format": "lrc",
        "codec_music_video": "h264-best",
        "quality_post": "best"
    }
    with open("config.json", "w") as f:
        json.dump(default_config, f, indent=4)

def read_config_file():
    with open("config.json", "r") as f:
        config_data = json.load(f)
        for key, value in config_data.items():
            if isinstance(value, str) and "_path" in key:
                # Handle path conversion based on OS
                if os.name == "posix":  # macOS
                    value = value.replace("//", "/")
                elif os.name == "nt":  # Windows
                    value = value.replace("\\", "\\")
            yield key, value

def save_config_file(config_data):
    for key, value in config_data.items():
        if isinstance(value, str) and "_path" in key:
            # Handle path conversion based on OS
            if os.name == "posix":  # macOS
                value = value.replace("/", "//")
            elif os.name == "nt":  # Windows
                value = value.replace("\\", "\\")

        # Check if the path refers to a drive on Windows
        if os.name == "nt" and key == "output_path":
            drive_letter = value.split("\\")[0]
            if not os.path.exists(drive_letter):
                raise ValueError(f"The specified drive '{drive_letter}' does not exist.")

        config_data[key] = value

    # Check if first folder/drive exists
    if os.name == "posix" and not os.path.exists(config_data["output_path"].split("/")[0]):
        os.makedirs(config_data["output_path"].split("/")[0])
    elif os.name == "nt" and not os.path.exists(config_data["output_path"].split("\\")[0]):
        os.makedirs(config_data["output_path"].split("\\")[0])

    with open("config.json", "w") as f:
        json.dump(config_data, f, indent=4)
