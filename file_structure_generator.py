import os
import argparse

def clean_line(line):
    """
    Removes tree structure characters (e.g., ├──, │, └──) and comments from a line.
    """
    # Remove tree structure characters
    line = line.replace("├──", "").replace("│", "").replace("└──", "").strip()
    # Remove comments (everything after #)
    line = line.split("#")[0].strip()
    return line

def create_file_structure(file_structure, output_folder):
    """
    Creates directories and files based on the provided file structure.

    Args:
        file_structure (str): A multi-line string representing the desired file structure.
                             Lines ending with `/` are treated as directories.
                             Other lines are treated as files.
        output_folder (str): The folder where the file structure will be created.
    """
    lines = file_structure.strip().split('\n')
    current_path = [output_folder]  # Start with the output folder as the base path

    for line in lines:
        # Clean the line by removing tree structure characters and comments
        line = clean_line(line)

        # Skip empty lines
        if not line:
            continue

        # Determine the indentation level
        # Count the number of leading spaces and divide by 4 (assuming 4 spaces per indent)
        indent_level = (len(line) - len(line.lstrip())) // 4
        line = line.strip()

        # Adjust the current path based on the indentation level
        current_path = current_path[:indent_level + 1]  # +1 to include the output folder

        if line.endswith('/'):
            # It's a directory
            dir_name = line[:-1]
            current_path.append(dir_name)
            os.makedirs(os.path.join(*current_path), exist_ok=True)
        else:
            # It's a file
            file_name = line
            file_path = os.path.join(*current_path, file_name)
            # Ensure the parent directory exists
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            open(file_path, 'a').close()

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
