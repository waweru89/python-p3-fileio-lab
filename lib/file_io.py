def write_file(file_name, file_content):
    """Writes content to a file."""
    with open(file_name, 'w') as f:
        f.write(file_content)

def append_file(file_name, append_content):
    """Appends content to a file."""
    with open(file_name, 'a') as f:
        f.write(append_content)

def read_file(file_name):
    """Reads content from a file."""
    with open(file_name, 'r') as f:
        return f.read()