import functools
import os

from jaraco.functools import compose
from jaraco.context import suppress


@functools.partial(compose, bool)
@suppress(FileNotFoundError)
def text_in_file(text, filename):
	return any(text in line for line in open(filename))


def is_docker():
	"""
	Is this current environment running in docker?

	>>> type(is_docker())
	<class 'bool'>
	"""
	return (
		os.path.exists('/.dockerenv')
		or text_in_file('docker', '/proc/self/cgroup')
	)
