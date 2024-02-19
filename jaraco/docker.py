import pathlib

from jaraco.functools import apply
from jaraco.context import suppress


@apply(bool)
@suppress(FileNotFoundError)
def text_in_file(text, filename: pathlib.Path):
    """
    >>> text_in_file('text in line', pathlib.Path(__file__))
    True
    """
    with filename.open(encoding='utf-8') as lines:
        return any(text in line for line in lines)


dockerenv = pathlib.Path('/.dockerenv')
cgroup = pathlib.Path('/proc/self/cgroup')


def is_docker():
    """
    Is this current environment running in docker?

    >>> type(is_docker())
    <class 'bool'>
    """
    return dockerenv.exists() or text_in_file('docker', cgroup)
