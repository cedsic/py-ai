# Py-AI Tools

![Python](https://img.shields.io/badge/Python-3.10+-blue) ![License](https://img.shields.io/badge/License-MIT-green)

**Python AI Tools Repository** – A collection of Python tools leveraging AI for practical tasks.

This repository contains lightweight, easy-to-use tools to get you started with AI development in Python.  
This repository is powered by: [Py.ai](https://py.ai)

---

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Tools](#tools)
- [Contributing](#contributing)
- [License](#license)
- [Links](#links)

---
## Installation

Clone this repository:

```bash
git clone git@github.com:cedsic/py-ai.git
cd py-ai
```

Create a virtual environment and install dependencies:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

Some of our resource are using OpenAI API. It is recommended to create a .env file in the root and add your OpenAI API key:

```
OPENAI_API_KEY=your_api_key_here
```

## Usage

The repository provides a unified CLI to access all tools. You can refer to the next section for the command to trigger each tool.

## Tools

### PDF Tools

1) **Extract text from a PDF:**  
  <u>Description</u>: Extracts plain text from PDFs.  
  <u>Location</u>: `py_ai/pdf_tools/extract_text.py`  
  <u>Trigger with the CLI</u>:
    ```bash
    python cli.py pdf extract /path/to/file.pdf
    ```

2) **Summarize a PDF using AI:**  
  <u>Description</u>: Summarizes PDFs using AI models (We are using the OpenAI API). Useful for quickly understanding long documents.  
  <u>Location</u>: `py_ai/pdf_tools/summarize_pdf.py`  
  <u>Trigger with the CLI</u>:
    ```bash
    python cli.py pdf summarize /path/to/file.pdf --max-chars 800
    ```

## Contributing

Contributions are welcome! You can add new Python AI tools following the same structure:

```
py-ai/tools_name/
├── __init__.py
├── module1.py
└── module2.py
```

Add CLI commands in `cli.py`.
Update `requirements.txt` if new dependencies are needed.

## License

This project is licensed under the MIT License.


## Links

This repository is powered by: [Py.ai](https://py.ai)
