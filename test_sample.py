import http.server
import socketserver
import tempfile
import threading
from pathlib import Path

from log_script import main
from download_all import download_files


def test_truth():
    """Simple sanity check to ensure test suite runs."""
    assert True


def test_readme_mentions_project_name():
    with open("README.md", "r", encoding="utf-8") as handle:
        contents = handle.read()
    assert "TestCollegamento" in contents
    assert "TestDiCollegamento" in contents


def test_script_logs_greeting(capsys):
    main()
    captured = capsys.readouterr()
    assert "CIAO GABRIELE" in captured.out


def test_download_preserves_binary_content(tmp_path):
    """Ensure binary downloads (e.g., SVG) are fully written."""

    with tempfile.TemporaryDirectory() as server_dir:
        server_root = Path(server_dir)
        svg_content = """<svg xmlns='http://www.w3.org/2000/svg' width='10' height='10'><rect width='10' height='10' fill='black'/></svg>"""
        text_content = "hello world"

        (server_root / "image.svg").write_text(svg_content, encoding="utf-8")
        (server_root / "file.txt").write_text(text_content, encoding="utf-8")

        class Handler(http.server.SimpleHTTPRequestHandler):
            def __init__(self, *args, **kwargs):  # noqa: D401,N802 - silence server logs
                """Serve files from the temporary directory without noisy logs."""

                super().__init__(*args, directory=server_root, **kwargs)

            def log_message(self, format, *args):
                pass

        with socketserver.TCPServer(("", 0), Handler) as httpd:
            port = httpd.server_address[1]
            thread = threading.Thread(target=httpd.serve_forever, kwargs={"poll_interval": 0.01})
            thread.daemon = True
            thread.start()

            try:
                base_url = f"http://localhost:{port}"
                downloads = download_files(
                    [f"{base_url}/image.svg", f"{base_url}/file.txt"],
                    tmp_path,
                )
            finally:
                httpd.shutdown()
                thread.join()

    svg_path, text_path = downloads
    assert svg_path.read_text(encoding="utf-8") == svg_content
    assert text_path.read_text(encoding="utf-8") == text_content
    assert svg_path.stat().st_size > 1
