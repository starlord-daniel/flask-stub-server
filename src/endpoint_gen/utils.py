# Helper function for reading file content
def read_file(file_path: str) -> str:
    ''' Read the content of a file '''
    with open(file_path, "rb") as file:
        text = file.read()
        return text
