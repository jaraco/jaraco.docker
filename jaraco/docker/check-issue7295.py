#!/usr/bin/env python

"""
Script for evaluating docker/for-mac#7295.

Run with ``python -m jaraco.docker.check-issue7295``.
"""

import subprocess
import sys


codes = dict(
    SIGSEGV=139,
    SIGABRT=134,
    OK=0,
)
code_names = {v: k for k, v in codes.items()}


def run_test():
    cmd = ['docker', 'run', '--platform', 'linux/amd64', 'jaraco/for-mac-issue-7295']
    proc = subprocess.run(cmd, capture_output=True)
    return proc.returncode


def run(n_runs=10):
    print(f"Running the command {n_runs} times")
    codes = [run_test() for n in range(n_runs)]
    results = [code_names.get(code, code) for code in codes]
    failures = list(filter(None, codes))
    n_failures = len(failures)
    successes = n_runs - n_failures
    pct = successes / n_runs
    print(f"Success {pct:.0%} {results}")


__name__ == '__main__' and run(*map(eval, sys.argv[1:]))
