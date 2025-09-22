from src.tools import create_parent_directory, create_children_directories


def main():

    new_parent_path = create_parent_directory()
    create_children_directories(new_parent_path)


if __name__ == "__main__":
    main()
