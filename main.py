import sys

sys.dont_write_bytecode = True

import argparse
import json
import os
import subprocess

COOKIE = os.getenv("COOKIE", "")
HOME_DIR = os.getenv("HOME", "")
DATA_PATH = os.getenv("DATA_PATH", "data.json")
OUTPUT_BASE_DIR = os.getenv("OUTPUT_BASE_DIR", f"{HOME_DIR}/Downloads/data")
START = int(os.getenv("START", 1))


def get_command(output_type: str) -> str:
    if output_type == "video":
        if COOKIE:
            return 'ffmpeg -headers "Cookie: %s" -i "{{URL}}" -c copy "{{OUTPUT_PATH}}"' % COOKIE
        else:
            return 'ffmpeg -i "{{URL}}" -c copy "{{OUTPUT_PATH}}"'
    elif output_type == "image":
        if COOKIE:
            return 'wget --header "cookie: %s" "{{URL}}" -O "{{OUTPUT_PATH}}"' % COOKIE
        else:
            return 'wget "{{URL}}" -O "{{OUTPUT_PATH}}"'
    else:
        raise ValueError(f"INVALID_OUTPUT_TYPE: {output_type}")


def download(data_list: list, input_type: str, output_type: str, command: str, output_dir: str = OUTPUT_BASE_DIR) -> None:
    os.makedirs(output_dir, exist_ok=True)
    if input_type == "simple":
        for i, url in enumerate(data_list):
            type_to_ext = {"video": "mp4", "image": "png"}
            output_path = os.path.join(output_dir, f"{START+i:04}.{type_to_ext[output_type]}")
            subprocess.run(command.replace("{{URL}}", url).replace("{{OUTPUT_PATH}}", output_path), shell=True, check=True)
    elif input_type == "standard":
        for url, output_filename in data_list:
            output_path = os.path.join(output_dir, output_filename)
            subprocess.run(command.replace("{{URL}}", url).replace("{{OUTPUT_PATH}}", output_path), shell=True, check=True)
    else:
        raise ValueError(f"INVALID_INPUT_TYPE: {input_type}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--data-type", choices=["list", "dict"], required=True)
    parser.add_argument("--input-type", choices=["simple", "standard"], required=True)
    parser.add_argument("--output-type", choices=["video", "image"], required=True)

    args = parser.parse_args()
    data_type = args.data_type
    input_type = args.input_type
    output_type = args.output_type

    data = json.load(open(DATA_PATH))
    command = get_command(output_type)

    if data_type == "list":
        download(data, input_type, output_type, command)

    if data_type == "dict":
        for dir_name, data_list in data.items():
            output_dir = os.path.join(OUTPUT_BASE_DIR, dir_name)
            download(data_list, input_type, output_type, command, output_dir)


if __name__ == "__main__":
    main()
