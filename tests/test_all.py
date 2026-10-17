import importlib
import subprocess
import types

from importlib_resources import files

import jaraco.docker


def test_mountinfo():
    info_file = files().joinpath('mountinfo')
    assert jaraco.docker.text_in_file('docker|overlay', info_file)


def test_check_issue_run_test(monkeypatch):
    check = importlib.import_module('jaraco.docker.check-issue7295')
    result = types.SimpleNamespace(returncode=139)
    monkeypatch.setattr(subprocess, 'run', lambda cmd, **kwargs: result)
    assert check.run_test() == 139
