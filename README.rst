.. image:: https://img.shields.io/pypi/v/jaraco.docker.svg
   :target: `PyPI link`_

.. image:: https://img.shields.io/pypi/pyversions/jaraco.docker.svg
   :target: `PyPI link`_

.. _PyPI link: https://pypi.org/project/jaraco.docker

.. image:: https://github.com/jaraco/jaraco.docker/workflows/Automated%20Tests/badge.svg
   :target: https://github.com/jaraco/jaraco.docker/actions?query=workflow%3A%22Automated+Tests%22
   :alt: Automated Tests

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black
   :alt: Code style: Black

.. .. image:: https://readthedocs.org/projects/skeleton/badge/?version=latest
..    :target: https://skeleton.readthedocs.io/en/latest/?badge=latest


Usage
=====

To determine if the current environment is running in docker::

	from jaraco.docker import is_docker
	is_docker()
