from pathlib import Path

import pytest


pytest_plugins = ["pytester"]


@pytest.fixture(autouse=True)
def load_plugin_in_pytester_runs(pytester):
    src_path = Path(__file__).resolve().parents[1] / "src"
    pytester.makeconftest(
        f"""
        import sys

        sys.path.insert(0, {str(src_path)!r})
        pytest_plugins = ["pytest_re.plugin"]
        """
    )
