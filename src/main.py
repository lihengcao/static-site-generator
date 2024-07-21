"""main"""

import os
import argparse
import markdown

INPUT_FOLDER = "_posts/"
OUTPUT_FOLDER = "docs/"

VERBOSE = False


def main():
    """entrypoint"""
    parse_args()
    convert_markdown()
    build_homepage()

def parse_args() -> None:
    parser = argparse.ArgumentParser(prog='static site generator')
    parser.add_argument('-i', '--input-folder')
    parser.add_argument('-o', '--output-folder')

    args = parser.parse_args()

    # This is horrible practice. I will change this... eventually...
    if args.input_folder is not None:
        global INPUT_FOLDER
        INPUT_FOLDER = args.input_folder
    if args.output_folder is not None:
        global OUTPUT_FOLDER
        OUTPUT_FOLDER = args.output_folder


def build_homepage() -> None:
    index_file = [
        "# Liheng's Blog\n",  # Some md linter tells me that there should be an *additional* new line afterwards
        "Made with my own simple static site generator ([repo](https://github.com/lihengcao/static-site-generator/))",
        "\n## Posts\n",  # same here. an additional newline before and after
        ]

    posts = get_posts_in_order()

    for date, name, filename in posts:
        index_file.extend([
            f"- [{date} {name}](./{filename})",
        ])

    index_file = "\n".join(index_file) + "\n"

    if VERBOSE:
        with open(INPUT_FOLDER + "index.md", "w", encoding="utf-8") as f:
            f.writelines(index_file)

    index_file = markdown.markdown(index_file)
    with open(OUTPUT_FOLDER + "index.html", "w", encoding="utf-8") as f:
        f.writelines(index_file)

def get_posts_in_order() -> list[tuple[str, str, str]]:
    files_in_output_directory = os.listdir(OUTPUT_FOLDER)
    posts = []

    for filename in files_in_output_directory:
        if not filename.endswith(".html") or filename == "index.html":
            continue

        name_only = filename[:-len(".html")]
        date, name = name_only.split('::')
        posts.append((date, name, filename))

    posts.sort(reverse=True)

    return posts


def convert_markdown() -> None:
    files_in_input_directory = os.listdir(INPUT_FOLDER)
    if VERBOSE:
        print(f"{files_in_input_directory=}")

    for filename in files_in_input_directory:
        if not filename.endswith(".md") or filename == "index.md":
            continue

        input_file = INPUT_FOLDER + filename

        filename_without_dotmd = filename[:-len(".md")]
        output_file = OUTPUT_FOLDER + filename_without_dotmd + ".html"

        markdown.markdownFromFile(input=input_file , output=output_file)


if __name__ == "__main__":
    main()
