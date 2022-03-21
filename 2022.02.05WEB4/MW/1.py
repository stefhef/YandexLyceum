import argparse


def print_error(message):
    print(f"ERROR: {message}!!")


if __name__ == "__main__":
    params = argparse.ArgumentParser()
    params.add_argument('message', default='', nargs='*')
    arg = params.parse_args()
    print("Welcome to my program")
    print_error(" ".join(arg.message))
