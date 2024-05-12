"""
This module contains reusable handy tools.
"""

from pathlib import Path


def check_file(file: str) -> bool:
    """Checks if the given file exists and if it has a '.pdf' extension.

    Args:
        file (str): The path of the file to be checked.

    Returns:
        bool: True if the file exists and has a '.pdf' extension, False otherwise.
    """

    file_exists: bool = Path(file).exists()
    file_is_pdf: bool = file.casefold().endswith(".pdf")
    return file_exists and file_is_pdf
