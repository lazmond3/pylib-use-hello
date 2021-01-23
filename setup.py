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
    name='lazmodn3-pylib-hello-world',
    version='1.0.0',
    description='Hello world package',
    long_description=readme,
    author='lazmond3',
    author_email='moikilo00@gmail.com',
    url='https://github.com/lazmond3/pylib-hello-world.git',
    install_requires=read_requirements(),
    license=license,
    entry_points={
        "console_scripts": [
            "pylib-hello-world=hello.cli:hello"
        ]
    },
    packages=find_packages(exclude=('tests', 'docs')),
    est_suite='tests'
)
