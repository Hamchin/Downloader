import sys

sys.dont_write_bytecode = True

import argparse
import os
import subprocess

from data import DATA_LIST

COOKIE = os.getenv("COOKIE", "")
OUTPUT_DIR = os.getenv("OUTPUT_DIR", "${HOME}/Downloads/data")
START = int(os.getenv("START", 1))

def get_command(mode: str) -> str:
    if mode == "video":
        if COOKIE:
            return 'ffmpeg -headers "Cookie: %s" -i "{{URL}}" -c copy "{{OUTPUT_PATH}}"' % COOKIE
        else:
            return 'ffmpeg -i "{{URL}}" -c copy "{{OUTPUT_PATH}}"'
    elif mode == "image":
        if COOKIE:
            return 'wget --header "cookie: %s" "{{URL}}" -O "{{OUTPUT_PATH}}"' % COOKIE
        else:
            return 'wget "{{URL}}" -O "{{OUTPUT_PATH}}"'
    else:
        raise ValueError(f"INVALID_MODE: {mode}")


def download(mode: str, data_type: str, command: str) -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    if data_type == "simple":
        for i, url in enumerate(DATA_LIST):
            mode_to_ext = {"video": "mp4", "image": "png"}
            output_path = os.path.join(OUTPUT_DIR, f"{START+i:04}.{mode_to_ext[mode]}")
            subprocess.run(command.replace("{{URL}}", url).replace("{{OUTPUT_PATH}}", output_path), shell=True, check=True)
    elif data_type == "standard":
        for url, output_filename in DATA_LIST:
            output_path = os.path.join(OUTPUT_DIR, output_filename)
            subprocess.run(command.replace("{{URL}}", url).replace("{{OUTPUT_PATH}}", output_path), shell=True, check=True)
    else:
        raise ValueError(f"INVALID_DATA_TYPE: {data_type}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=["video", "image"], required=True)
    parser.add_argument("--data-type", choices=["simple", "standard"], required=True)

    args = parser.parse_args()
    mode = args.mode
    data_type = args.data_type

    command = get_command(mode)
    download(mode, data_type, command)
