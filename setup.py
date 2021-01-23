# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages
import os


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()


def read_requirements():
    """Parse requirements from requirements.txt."""
    reqs_path = os.path.join('.', 'requirements.txt')
    with open(reqs_path, 'r') as f:
        requirements = [line.rstrip() for line in f]
    return requirements


setup(
    name='lazmodn3-pylib-use-hello',
    version='1.0.0',
    description='using Hello',
    long_description=readme,
    author='lazmond3',
    author_email='moikilo00@gmail.com',
    url='https://github.com/lazmond3/pylib-use-hello.git',
    install_requires=read_requirements(),
    license=license,
    entry_points={
        "console_scripts": [
            "pylib-use-hello=use_hello.cli:hello"
        ]
    },
    packages=find_packages(exclude=('tests', 'docs')),
    test_suite='tests'
)
