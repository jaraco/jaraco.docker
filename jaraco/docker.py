import pathlib

from jaraco.functools import apply
from jaraco.context import suppress


@apply(bool)
@suppress(FileNotFoundError)
def text_in_file(text, filename):
    return any(text in line for line in filename.open())


dockerenv = pathlib.Path('/.dockerenv')
cgroup = pathlib.Path('/proc/self/cgroup')


def is_docker():
    """
    Is this current environment running in docker?

    >>> type(is_docker())
    <class 'bool'>
    """
    return dockerenv.exists() or text_in_file('docker', cgroup)
