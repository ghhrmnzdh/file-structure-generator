import os
import argparse

def clean_and_parse_line(line, indent_size=4):
    """
    Remove tree drawing characters while preserving the indentation.
    Returns a tuple (level, name), where 'level' is the depth based on the 
    number of leading spaces (divided by indent_size) and 'name' is the actual 
    file or directory name.
    """
    # Replace tab characters with fixed number of spaces.
    line = line.replace("\t", " " * indent_size)
    # Replace tree drawing vertical bars with spaces.
    line = line.replace("│", " " * indent_size)
    # Remove branch markers.
    line = line.replace("├──", "").replace("└──", "")
    
    # Calculate the indentation level.
    stripped = line.lstrip()
    indent = len(line) - len(stripped)
    level = indent // indent_size
    return level, stripped.rstrip()  # remove trailing spaces or newline

def create_file_structure(structure_str, output_folder):
    """
    Create the file and directory structure based on a multi-line string.
    
    Each line ending with '/' indicates a directory; otherwise, it is a file.
    The first line is assumed to represent a "project" root and is ignored, 
    using the output folder as the actual root.
    """
    # Split the input into individual lines.
    lines = structure_str.strip().splitlines()
    if not lines:
        print("Input structure is empty.")
        return

    # Ensure the output folder exists.
    os.makedirs(output_folder, exist_ok=True)

    # If the first line represents the project root (ends with '/'),
    # ignore it and use the output folder as the root.
    if lines[0].strip().endswith('/'):
        print(f"Ignoring the provided root '{lines[0].strip()}' and using '{output_folder}' as project root.")
        lines = lines[1:]

    # Use a stack to track parent directories. Each element in the stack
    # is a tuple: (indent_level, absolute_path). The stack starts with our output folder.
    stack = [( -1, output_folder )]  # use -1 so that first level (0) is appended properly

    for line in lines:
        # Skip empty lines.
        if not line.strip():
            continue

        level, name = clean_and_parse_line(line)
        if not name:
            continue

        # Ensure the stack only contains the parent directories of the current level.
        while stack and stack[-1][0] >= level:
            stack.pop()

        # The parent directory for the current item:
        parent_path = stack[-1][1]
        current_path = os.path.join(parent_path, name.rstrip("/"))

        if name.endswith('/'):  # It's a directory.
            os.makedirs(current_path, exist_ok=True)
            print(f"Created directory: {current_path}")
            # Append the new directory with its level (current level becomes parent's level for its children)
            stack.append((level, current_path))
        else:
            # It's a file.
            os.makedirs(parent_path, exist_ok=True)
            with open(current_path, 'w') as f:
                f.write(f"Placeholder content for {current_path}\n")
            print(f"Created file: {current_path}")

    print(f"File structure created successfully in '{output_folder}'.")

def main():
    parser = argparse.ArgumentParser(
        description="Generate a file structure from a multi-line string input."
    )
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
    create_file_structure(args.input, args.output)

if __name__ == "__main__":
    main()
