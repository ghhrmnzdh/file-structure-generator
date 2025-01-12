# File Structure Generator

File Structure Generator is a lightweight Python utility that dynamically creates file and directory structures from user input. It is designed to help developers quickly set up organized project templates—supporting nested directories, CLI flexibility, and even AI-generated file structures.

## Features

- **Dynamic Structure Creation:** Generate directories and files from a multi-line string input.
- **Nested Directory Support:** Easily create deeply nested hierarchies.
- **Customizable:** Adapt the input format to suit your specific project needs.
- **Lightweight & Dependency-Free:** Written in pure Python—no external libraries required.
- **Command-Line Interface (CLI):** Define the file structure and target output folder directly from the command line.

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/ghhrmnzdh/file-structure-generator.git
   cd file-structure-generator
   ```

2. **Verify Python Installation:**
   
   Ensure you have Python 3.6 or later installed on your system.

3. **Run the Script:**

   ```bash
   python file_structure_generator.py --input "your-file-structure" --output "your-folder"
   ```

## Usage

### 1. Define Your File Structure

Pass the file structure as a multi-line string using the `--input` argument. The format to follow is:

- **Directories:** Lines ending with a forward slash (`/`) are interpreted as directories.
- **Files:** All other lines are treated as files.
- **Indentation:** Use 4 spaces per level to define nested relationships.

### 2. Specify the Output Folder

Use the `--output` argument to designate the folder where the file structure will be created. The script will automatically create the folder if it does not already exist.

### 3. Execute the Script

Run the script with your parameters. For example:

```bash
python file_structure_generator.py \
    --input "
my-project/
├── README.md
├── main.py
├── utils/
│   ├── __init__.py
│   └── file_utils.py
└── tests/
    ├── __init__.py
    └── test_main.py
" \
    --output "my-project-folder"
```

## Examples

### Example 1: Web Application

```bash
python file_structure_generator.py \
    --input "
web-app/
├── README.md
├── app/
│   ├── __init__.py
│   ├── routes.py
│   └── templates/
│       ├── index.html
│       └── about.html
├── static/
│   ├── css/
│   │   └── styles.css
│   └── js/
│       └── script.js
└── tests/
    ├── __init__.py
    └── test_routes.py
" \
    --output "web-app-folder"
```

**Resulting Structure:**

```
web-app-folder/
├── README.md
├── app/
│   ├── __init__.py
│   ├── routes.py
│   └── templates/
│       ├── index.html
│       └── about.html
├── static/
│   ├── css/
│   │   └── styles.css
│   └── js/
│       └── script.js
└── tests/
    ├── __init__.py
    └── test_routes.py
```

### Example 2: CLI Tool

```bash
python file_structure_generator.py \
    --input "
cli-tool/
├── README.md
├── cli/
│   ├── __init__.py
│   ├── main.py
│   └── commands/
│       ├── init.py
│       └── run.py
└── tests/
    ├── __init__.py
    └── test_cli.py
" \
    --output "cli-tool-folder"
```

**Resulting Structure:**

```
cli-tool-folder/
├── README.md
├── cli/
│   ├── __init__.py
│   ├── main.py
│   └── commands/
│       ├── init.py
│       └── run.py
└── tests/
    ├── __init__.py
    └── test_cli.py
```

### Example 3: Deeply Nested Project

```bash
python file_structure_generator.py \
    --input "
nested-project/
├── README.md
├── src/
│   ├── __init__.py
│   ├── api/
│   │   ├── __init__.py
│   │   ├── v1/
│   │   │   ├── __init__.py
│   │   │   ├── endpoints.py
│   │   │   └── models.py
│   │   └── v2/
│   │       ├── __init__.py
│   │       ├── endpoints.py
│   │       └── models.py
│   └── utils/
│       ├── __init__.py
│       ├── file_utils.py
│       └── math_utils.py
└── tests/
    ├── __init__.py
    ├── test_api/
    │   ├── __init__.py
    │   ├── test_v1.py
    │   └── test_v2.py
    └── test_utils/
        ├── __init__.py
        └── test_file_utils.py
" \
    --output "nested-project-folder"
```

**Resulting Structure:**

```
nested-project-folder/
├── README.md
├── src/
│   ├── __init__.py
│   ├── api/
│   │   ├── __init__.py
│   │   ├── v1/
│   │   │   ├── __init__.py
│   │   │   ├── endpoints.py
│   │   │   └── models.py
│   │   └── v2/
│   │       ├── __init__.py
│   │       ├── endpoints.py
│   │       └── models.py
│   └── utils/
│       ├── __init__.py
│       ├── file_utils.py
│       └── math_utils.py
└── tests/
    ├── __init__.py
    ├── test_api/
    │   ├── __init__.py
    │   ├── test_v1.py
    │   └── test_v2.py
    └── test_utils/
        ├── __init__.py
        └── test_file_utils.py
```

## Benefits

### Time Savings

Automate the creation of complex directory structures, allowing you to focus on development rather than manual setup.

### Consistent Organization

Maintain a standardized project structure, which simplifies project navigation and maintenance, whether you’re working solo or in a team environment.

### Zero Dependencies

Enjoy a streamlined solution written entirely in Python without any additional libraries—simply clone the repository and get started.

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m 'Add your feature'`
4. Push to the branch: `git push origin feature/your-feature`
5. Open a pull request with a detailed description of your changes.

## Support

If you find File Structure Generator useful, please consider giving the project a star on GitHub. Your support is greatly appreciated and motivates further development.

## Contact

For questions or feedback, please open an issue on GitHub or contact the project maintainer directly.
