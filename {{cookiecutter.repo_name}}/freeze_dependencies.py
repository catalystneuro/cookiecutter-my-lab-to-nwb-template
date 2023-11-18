import os


def main():
    os.system("pip freeze > frozen_dependencies.txt")


if __name__ == "__main__":
    main()
