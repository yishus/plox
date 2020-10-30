import sys

from scanner import scan


def main():
    if len(sys.argv) > 2:
        print("Usage: python3 plox [script]")
    elif len(sys.argv) == 2:
        run_file(sys.argv[1])
    else:
        run_prompt()


def run_file(filename):
    with open(filename, "r") as reader:
        run(reader.read())


def run_prompt():
    while True:
        line = input("> ")
        run(line)


def run(source):
    scan(source)
