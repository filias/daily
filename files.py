import sys


def main():
    with open("resources/text.txt") as file:
        lines = file.read().splitlines()
        lines.reverse()
        for line in lines:
            sys.stdout.write(line[::-1] + "\n")


if __name__ == "__main__":
    main()
