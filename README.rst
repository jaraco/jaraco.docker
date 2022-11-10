.. image:: https://img.shields.io/pypi/v/jaraco.docker.svg
   :target: https://pypi.org/project/jaraco.docker

.. image:: https://img.shields.io/pypi/pyversions/jaraco.docker.svg

.. image:: https://github.com/jaraco/jaraco.docker/workflows/tests/badge.svg
   :target: https://github.com/jaraco/jaraco.docker/actions?query=workflow%3A%22tests%22
   :alt: tests

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black
   :alt: Code style: Black

.. .. image:: https://readthedocs.org/projects/skeleton/badge/?version=latest
..    :target: https://skeleton.readthedocs.io/en/latest/?badge=latest

.. image:: https://img.shields.io/badge/skeleton-2022-informational
   :target: https://blog.jaraco.com/skeleton

Usage
=====

To determine if the current environment is running in docker::

	from jaraco.docker import is_docker
	is_docker()
