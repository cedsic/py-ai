import pytest
from py_ai.core import summarize_file
from pathlib import Path


PDF_FILE = Path("test_input/test.pdf")
CSV_FILE = Path("test_input/test.xlsx")
PNG_FILE = Path("test_input/test.png")
PNG_FILE2 = Path("test_input/test2.png")

@pytest.mark.parametrize("file_path", [PDF_FILE, CSV_FILE, PNG_FILE, PNG_FILE2])
def test_summarize_file(file_path):
    """
    Test that summarize_file returns a non-empty string for all supported file types.
    """
    summary = summarize_file(file_path, max_chars=200)
    assert isinstance(summary, str)
    assert len(summary) > 0

def test_file_not_found():
    """
    Test that summarize_file raises FileNotFoundError for missing files.
    """
    with pytest.raises(FileNotFoundError):
        summarize_file("nonexistent.file")

def test_unsupported_file():
    """
    Test that summarize_file raises ValueError for unsupported file types.
    """
    unsupported_file = Path("test_input/unsupported.txt")
    unsupported_file.touch()  # create empty file
    try:
        with pytest.raises(ValueError):
            summarize_file(unsupported_file)
    finally:
        unsupported_file.unlink()  # clean up
