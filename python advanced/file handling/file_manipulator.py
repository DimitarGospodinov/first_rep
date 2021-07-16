import os


def manage_file(file_path, mode, content=None):
    with open(file_path, mode) as file:
        if content:
            return file.write(content + "\n")
        return file.write("")


def create_file(file_path):
    manage_file(file_path, "r+")


def add_content_to_file(file_path, content):
    manage_file(file_path, "a", content)


def replace_content_file(file_path, content, replace_with):
    try:
        with open(file_path, "r+") as file:
            text = "".join(file.readlines())
            replaced_content = text.replace(content, replace_with)
            file.seek(0)
            file.write(replaced_content)
    except FileNotFoundError:
        print("An error occurred")


def delete_file(file_path):
    try:
        os.remove(file_path)
    except FileNotFoundError:
        print("An error occurred")


actioner = {"Create": create_file,
            "Add": add_content_to_file,
            "Replace": replace_content_file,
            "Delete": delete_file}


def start_engine():
    command_data = input().split("-")
    while command_data[0] != "End":
        command, command_args = command_data[0], command_data[1:]
        actioner[command](*command_args)
        command_data = input().split("-")


start_engine()
