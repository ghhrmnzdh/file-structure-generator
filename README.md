# File Structure Generator 🚀

A Python script to dynamically generate file structures based on user input. Perfect for developers to quickly create organized project templates. Supports nested directories, customizable inputs, and command-line flexibility.

---

## Features ✨

- **Dynamic File Structure Creation**: Generate directories and files from a multi-line string input.
- **Nested Structures**: Supports deeply nested directory hierarchies.
- **Customizable**: Easily adapt the input to match your project's needs.
- **Lightweight**: No dependencies—just pure Python.
- **Command-Line Interface (CLI)**: Specify the file structure and output folder directly when running the script.

---

## Installation 📥

1. Clone the repository:
   ```bash
   git clone https://github.com/ghhrmnzdh/file-structure-generator.git
   cd file-structure-generator
   ```

2. Ensure you have Python installed (Python 3.6 or higher).

3. Run the script:
   ```bash
   python file_structure_generator.py --input "your-file-structure" --output "your-folder"
   ```

---

## Usage 🛠️

### Step 1: Define Your File Structure
Provide the file structure as a multi-line string using the `--input` argument. Use the following format:
- Lines ending with `/` are treated as **directories**.
- Other lines are treated as **files**.
- Use indentation (4 spaces) to define nested structures.

### Step 2: Specify the Output Folder
Use the `--output` argument to specify the folder where the file structure will be created. If the folder doesn’t exist, it will be created automatically.

### Step 3: Run the Script
Execute the script with your input and output arguments. For example:
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

---

## Examples 🚀

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

**Output Structure**:
```
web-app-folder/
│
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

---

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

**Output Structure**:
```
cli-tool-folder/
│
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

---

### Example 3: Nested Structure (Working!)
This example demonstrates a deeply nested file structure:
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

**Output Structure**:
```
nested-project-folder/
│
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

---

## Why Use This Tool? 💡

### Save Time ⏳
Manually creating directories and files for a new project can be tedious. This tool automates the process, allowing you to focus on writing code instead of setting up folders.

### Stay Organized 🗂️
A well-structured project is easier to navigate and maintain. This tool ensures consistency across your projects, whether you're working alone or in a team.

### No Dependencies 🚀
The script is written in pure Python, so you don’t need to install any additional libraries. Just clone the repository and start using it!

---

## Contributing 🤝

Contributions are welcome! If you have ideas for improvements or new features, please:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request.

---

## Support 🌟

If you find this tool helpful, please give it a ⭐ on GitHub! Your support encourages further development and improvements.

---

## Questions or Feedback? 💬

Feel free to open an issue on the repository or reach out to me directly. Let’s build something amazing together! 🚀
