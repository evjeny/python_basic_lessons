import argparse
import os
from base64 import b64encode


template = """from base64 import b64decode

def main():
    data = "{encoded}"
    script = b64decode(data.encode("utf-8")).decode("utf-8")
    exec(script)


if __name__ == "__main__":
    main()
"""


def encode_file(python_content: str) -> str:
    global template

    encoded = b64encode(python_content.encode("utf-8")).decode("utf-8")
    return template.format(encoded=encoded)


def main(folder: str, prefix="unsafe_", postfix=".py"):
    for fname in os.listdir(folder):
        if not (fname.startswith(prefix) and fname.endswith(postfix)):
            continue
        with open(os.path.join(folder, fname)) as f:
            content = f.read()
        
        with open(os.path.join(folder, fname.replace(prefix, "")), "w+") as f:
            f.write(encode_file(content))


if __name__ == "__main__":
    parser = argparse.ArgumentParser("Test converter")
    parser.add_argument("--folder", type=str, help="path to folder")
    args = parser.parse_args()

    main(args.folder)
