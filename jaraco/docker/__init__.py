from __future__ import annotations

import itertools
import pathlib
import re

from jaraco.functools import apply
from jaraco.context import suppress


@apply(bool)
@suppress(FileNotFoundError)
def text_in_file(text: str, filename: pathlib.Path, limit: int | None = None) -> bool:
    """
    >>> text_in_file('anything', pathlib.Path(__file__))
    True
    >>> text_in_file('bomb'*2, pathlib.Path(__file__))
    False
    >>> text_in_file('anything', pathlib.Path('/doesnotexist'))
    False
    """
    with filename.open(encoding='utf-8') as lines:
        return any(re.search(text, line) for line in itertools.islice(lines, limit))


dockerenv = pathlib.Path('/.dockerenv')
cgroup = pathlib.Path('/proc/self/cgroup')
mountinfo = pathlib.Path('/proc/self/mountinfo')


def is_docker() -> bool:
    """
    Is this current environment running in docker?

    >>> type(is_docker())
    <class 'bool'>
    """
    return (
        dockerenv.exists()
        or text_in_file('docker', cgroup)
        or text_in_file('docker|overlay', mountinfo, limit=1)
    )
