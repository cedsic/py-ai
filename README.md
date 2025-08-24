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

### Image Tools

1) **Extract text from an image:**  
  <u>Description:</u> Extracts plain text from images using Python (OpenCV + pytesseract). Useful for scanned documents, screenshots, or any image containing text.  
  <u>Location:</u> `py_ai/image_tools/extract_text.py`  
  <u>Trigger with the CLI:</u>
    ```bash
    python cli.py image extract /path/to/file.png
    ```

2) **Summarize an image using AI:**  
  <u>Description:</u> First extracts text from an image, then summarizes it using AI models (OpenAI API). Ideal for quickly understanding text-heavy images.  
  <u>Location:</u> `py_ai/image_tools/summarize_image.py`  
  <u>Trigger with the CLI:</u>
    ```bash
    python cli.py image summarize /path/to/file.png --max-chars 800
    ```

**Notes:**  
Make sure Tesseract OCR is installed on your system (`sudo apt install tesseract-ocr`) and available in your PATH.  

## Contributing

At this time, this repository is **not accepting external contributions**.  
We may consider contributions in the future, so stay tuned!

If you find issues or have suggestions, you can [contact us](https://py.ai/contact-us/).

## License

This project is licensed under the MIT License.


## Links

This repository is powered by: [Py.ai](https://py.ai)
