import importlib.util
import pathlib


def test_can_import_server_module():
    repo_root = pathlib.Path(__file__).resolve().parents[2]
    server_path = repo_root / "app" / "server.py"

    spec = importlib.util.spec_from_file_location("lab2_server", server_path)
    assert spec is not None

    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)

    assert hasattr(module, "main")
