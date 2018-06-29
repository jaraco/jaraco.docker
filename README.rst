.. image:: https://img.shields.io/pypi/v/jaraco.docker.svg
   :target: https://pypi.org/project/jaraco.docker

.. image:: https://img.shields.io/pypi/pyversions/jaraco.docker.svg

.. image:: https://img.shields.io/travis/jaraco/jaraco.docker/master.svg
   :target: https://travis-ci.org/jaraco/jaraco.docker

.. .. image:: https://img.shields.io/appveyor/ci/jaraco/jaraco.docker/master.svg
..    :target: https://ci.appveyor.com/project/jaraco/jaraco.docker/branch/master

.. .. image:: https://readthedocs.org/projects/jaracodocker/badge/?version=latest
..    :target: https://jaracodocker.readthedocs.io/en/latest/?badge=latest


Usage
=====

To determine if the current environment is running in docker::

	from jaraco.docker import is_docker
	is_docker()
