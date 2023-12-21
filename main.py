"""main"""

INPUT = "input.md"
OUTPUT = "index.html"


def main() -> None:
    """entrypoint"""
    lines = read_file()

    lines = [convert_line(line) for line in lines]

    write_file(lines)


def convert_line(line: str) -> str:
    """convert input line into html output, kind of"""
    ind = 0
    while ind < len(line):
        if line[ind] != "#":
            break
        ind += 1

    if ind == 0:
        return line

    return f"<h{ind}>" + line[ind + 1 :].rstrip() + f"</h{ind}>\n"


def read_file() -> list[str]:
    """read file ... """
    with open(INPUT, "r", encoding="utf-8") as f:
        # return f.read().splitlines()
        return f.readlines()


def write_file(lines: list[str]) -> None:
    """write file ..."""
    with open(OUTPUT, "w", encoding="utf-8") as f:
        f.writelines(lines)


if __name__ == "__main__":
    main()
