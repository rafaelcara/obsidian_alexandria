import os
from src.config import PARENT_PATH, CONTENTS


def generate_directory_names(contents):
    return [f"{k:>02}_{v}" for k, v in contents.items()]


def make_directory(directory_name, parent_path):
    full_path = os.path.join(parent_path, directory_name)
    os.makedirs(full_path, exist_ok=True)


def create_parent_directory():
    directory_name = "computer_science/"
    make_directory(directory_name, PARENT_PATH)
    return os.path.join(PARENT_PATH, directory_name)


def create_children_directories(new_parent_path):
    list_names = generate_directory_names(CONTENTS)

    for name in list_names:
        make_directory(name, new_parent_path)
