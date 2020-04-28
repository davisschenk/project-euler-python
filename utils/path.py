from pathlib import Path


def load_file(name):
    path = (Path(__file__).parent / f"../files/{name}").resolve()
    return open(path)