import os
from flask import request
import pytest


@pytest.fixture(scope="session", autouse=True)
def clear_db(request):
    from pathlib import Path
    path = os.path.join(Path(os.getcwd()), 'apps\\db.sqlite3')
    if os.path.exists(path):
        os.remove(path)
