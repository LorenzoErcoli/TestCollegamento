"""Utility for downloading files while preserving binary content."""
from __future__ import annotations

import os
import pathlib
import urllib.request
from typing import Iterable


def _ensure_output_dir(output_dir: os.PathLike | str) -> pathlib.Path:
    """Return an existing output directory, creating it if missing."""
    path = pathlib.Path(output_dir)
    path.mkdir(parents=True, exist_ok=True)
    return path


def download_file(url: str, output_dir: os.PathLike | str) -> pathlib.Path:
    """Download a single file from ``url`` into ``output_dir``.

    The file is written in binary mode to avoid truncating binary assets such as SVGs.
    A ``ValueError`` is raised if the response body is empty.
    """

    output_path = _ensure_output_dir(output_dir) / pathlib.Path(urllib.request.urlsplit(url).path).name
    with urllib.request.urlopen(url) as response:
        content = response.read()

    if not content:
        raise ValueError(f"No content received from {url}")

    with open(output_path, "wb") as handle:
        handle.write(content)

    return output_path


def download_files(urls: Iterable[str], output_dir: os.PathLike | str) -> list[pathlib.Path]:
    """Download all files from ``urls`` into ``output_dir``.

    Returns a list of paths to the downloaded files.
    """

    return [download_file(url, output_dir) for url in urls]


__all__ = ["download_file", "download_files"]
