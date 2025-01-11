import os
import argparse

def clean_line(line):
    """
    Removes tree structure characters and comments from a line, replacing tabs with four spaces.
    """
    line = line.replace("├──", "").replace("│", "").replace("└──", "").replace("\t", "    ")
    line = line.split("#")[0]
    return line

def detect_indentation_size(lines):
    """
    Detects the number of spaces used for indentation in the file structure.
    Defaults to 4 spaces if no indentation is detected.
    """
    for line in lines:
        stripped_line = line.lstrip()
        if stripped_line and not stripped_line.startswith("#"):
            indentation = len(line) - len(stripped_line)
            if indentation > 0:
                return indentation
    return 4  # Default to 4 spaces if no indentation is detected

def create_file_structure(file_structure, output_folder):
    """
    Creates directories and files based on the provided file structure.

    Args:
        file_structure (str): A multi-line string representing the desired file structure.
                              Lines ending with '/' are treated as directories.
                              Other lines are treated as files.
        output_folder (str): The folder where the file structure will be created.
    """
    lines = file_structure.strip().split('\n')

    # Detect the indentation size
    indentation_size = detect_indentation_size(lines)
    if indentation_size == 0:
        indentation_size = 4  # Fallback to 4 spaces if indentation size is 0

    # Initialize stack with the output folder
    stack = [output_folder]

    # Identify the root directory
    root_dir_line = clean_line(lines[0])
    if root_dir_line.endswith('/'):
        root_dir = root_dir_line[:-1]
    else:
        root_dir = root_dir_line

    # Create root directory inside the output folder
    root_dir_path = os.path.join(output_folder, root_dir)
    os.makedirs(root_dir_path, exist_ok=True)
    stack.append(root_dir)

    # Skip the root directory line
    lines = lines[1:]

    for line in lines:
        # Clean the line without stripping to preserve leading spaces
        clean = clean_line(line)

        # Skip empty lines
        if not clean.strip():
            continue

        # Determine the indentation level based on leading spaces
        indent_level = (len(clean) - len(clean.lstrip())) // indentation_size

        # Adjust the stack to the current indentation level
        while len(stack) > indent_level + 1:
            stack.pop()

        # Remove leading spaces to get the actual item name
        item_name = clean.lstrip()

        if item_name.endswith('/'):
            # It's a directory
            dir_name = item_name[:-1]
            dir_path = os.path.join(*stack, dir_name)
            os.makedirs(dir_path, exist_ok=True)
            stack.append(dir_name)
            print(f"Created directory: {dir_path}")
        else:
            # It's a file
            file_path = os.path.join(*stack, item_name)
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            with open(file_path, 'w') as f:
                f.write(f"Placeholder content for {file_path}\n")
            print(f"Created file: {file_path}")

def main():
    # Set up argument parsing
    parser = argparse.ArgumentParser(description="Generate a file structure from a multi-line string input.")
    parser.add_argument(
        "--input",
        type=str,
        required=True,
        help="Multi-line string representing the file structure."
    )
    parser.add_argument(
        "--output",
        type=str,
        required=True,
        help="Folder where the file structure will be created."
    )
    args = parser.parse_args()

    # Create the file structure
    create_file_structure(args.input, args.output)
    print(f"File structure created successfully in '{args.output}'.")

if __name__ == "__main__":
    main()