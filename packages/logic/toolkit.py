"""
This module contains reusable handy tools.
"""

from pathlib import Path

import pdfrw


def check_file(file: str) -> bool:
    """Checks if the given file exists and if it has a '.pdf' extension.

    Args:
        file (str): The path of the file to be checked.

    Returns:
        bool: True if the file exists and has a '.pdf' extension, False otherwise.
    """

    return Path(file).exists() and file.casefold().endswith(".pdf")


def overwrite_metadata(new_location: tuple[Path, str], file: pdfrw.PdfReader, metadata: dict) -> bool:
    """Overwrites the metadata of a PDF file with new metadata.

    Args:
        new_location (tuple[Path, str]): A tuple containing the new location information.
        file (pdfrw.PdfReader): The PDF file to modify.
        metadata (dict): A dictionary containing the metadata tags and their corresponding values to be overwritten.

    Returns:
        bool: True if the PDF file was successfully saved with the new metadata; False otherwise.
    """

    old_path, new_name = new_location

    if not (old_path.exists() and new_name):
        return False
    destination: Path = Path.joinpath(old_path.parent, f"{new_name}.pdf")

    for tag, value in metadata.items():
        setattr(file.Info, tag, value)
    pdfrw.PdfWriter(destination, trailer=file).write()

    if destination.exists():
        return True
    return False
