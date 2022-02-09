import argparse


def count_lines(filename):
    try:
        with open(filename, "r") as file_input:
            lines = file_input.readlines()
    except Exception:
        lines = []
    return len(lines)


if __name__ == '__main__':
    params = argparse.ArgumentParser()
    params.add_argument('--file', default="")
    args = params.parse_args()
    print(count_lines(args.file))
