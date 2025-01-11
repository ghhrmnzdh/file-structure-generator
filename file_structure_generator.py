import os

def create_file_structure(file_structure):
    """
    Creates directories and files based on the provided file structure.

    Args:
        file_structure (str): A multi-line string representing the desired file structure.
                             Lines ending with `/` are treated as directories.
                             Other lines are treated as files.
    """
    lines = file_structure.strip().split('\n')
    current_path = []

    for line in lines:
        # Determine the indentation level
        indent_level = (len(line) - len(line.lstrip())) // 4  # Assuming 4 spaces per indent
        line = line.strip()

        if line.endswith('/'):
            # It's a directory
            dir_name = line[:-1]
            current_path = current_path[:indent_level]
            current_path.append(dir_name)
            os.makedirs(os.path.join(*current_path), exist_ok=True)
        else:
            # It's a file
            file_name = line.split('#')[0].strip()  # Ignore comments after #
            current_path = current_path[:indent_level]
            file_path = os.path.join(*current_path, file_name)
            open(file_path, 'a').close()

if __name__ == "__main__":
    # Example file structure input
    file_structure = """
    project-name/
    │
    ├── README.md               # Project documentation
    ├── requirements.txt        # Python dependencies
    ├── main.py                 # Main script
    ├── utils/                  # Utility functions
    │   ├── __init__.py
    │   ├── file_utils.py       # File handling utilities
    │   └── math_utils.py       # Math utilities
    │
    ├── config/                 # Configuration files
    │   ├── settings.json       # Application settings
    │   └── constants.py        # Constants
    │
    ├── logs/                   # Log files
    │   └── app_logs.log
    │
    └── tests/                  # Test cases
        ├── __init__.py
        ├── test_utils.py       # Tests for utility functions
        └── test_main.py        # Tests for main script
    """

    create_file_structure(file_structure)
    print("File structure created successfully.")
