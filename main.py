"""main"""

INPUT = "input.md"
OUTPUT = "index.html"

VERBOSE = True


def main():
    """entrypoint"""
    lines = read_file()

    lines = [convert_line(line) for line in lines]

    if VERBOSE:
        for line in lines:
            print(line, end="")

    write_file(lines)


def convert_line(line: str) -> str:
    """convert input line into html output, kind of"""
    line = line.lstrip()

    h_ind = 0  # header index
    while h_ind < len(line):
        if line[h_ind] != "#":
            break
        h_ind += 1

    if h_ind == 0:
        return line.rstrip() + "\n"

    content = line[h_ind + 1 :].rstrip()
    if len(content) == 0:
        return ""

    return f"<h{h_ind}>{content}</h{h_ind}>\n"


def read_file() -> list[str]:
    """read file ..."""
    with open(INPUT, "r", encoding="utf-8") as f:
        # return f.read().splitlines()
        return f.readlines()


def write_file(lines: list[str]) -> None:
    """write file ..."""
    with open(OUTPUT, "w", encoding="utf-8") as f:
        f.writelines(lines)


if __name__ == "__main__":
    main()
