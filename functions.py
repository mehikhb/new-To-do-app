def get_todos(filepath="todos.txt"):
    """ Read the text file content and
     return the values."""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_local,filepath="todos.txt"):
    """ Create a file and write the content in it."""
    with open(filepath, 'w') as file:
        file.writelines(todos_local)

