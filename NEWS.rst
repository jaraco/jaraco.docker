v2.3.0
======

Features
--------

- Add script for evaluating docker/for-mac#7295. (#7295)


v2.2.1
======

Bugfixes
--------

- Add a type annotation for the limit parameter of text_in_file.


v2.2.0
======

Features
--------

- Docker detection also looks for 'docker' or 'overlay' in the mount info. (#3)


v2.1.2
======

No significant changes.


v2.1.1
======

Bugfixes
--------

- Fixed ResourceWarning when opening the file.


v2.1.0
======

Packaging refresh.

Minor tweaks to use more modern abstractions (``pathlib``, ``jaraco.functools.apply``).

2.0
===

Switch to `pkgutil namespace technique
<https://packaging.python.org/guides/packaging-namespace-packages/#pkgutil-style-namespace-packages>`_
for the ``jaraco`` namespace.

1.0
===

Initial implementation with ``is_docker`` function.
