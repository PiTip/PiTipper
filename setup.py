#!/usr/bin/env python
from setuptools import setup, find_packages

# Little hack to make 'python setup.py test' work on py2.7
try:
    import multiprocessing
    import logging
    assert logging
    assert multiprocessing
except:
    pass


setup(
    name='pitipper',
    version="0.1",
    description="",
    author="",
    author_email="",
    url="",
    license="",
    install_requires=["praw"],
    packages=find_packages(exclude=['ez_setup', 'tests']),
    platforms=["any"],
    tests_require = ['coverage'],
    test_suite="tests",
    classifiers=[
            "Programming Language :: Python",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 2.6",
            "Programming Language :: Python :: 2.7",
            "Programming Language :: Python :: 3.2",
            "Programming Language :: Python :: 3.3",
            "License :: OSI Approved :: BSD License",
            "Topic :: Software Development :: Libraries :: Python Modules",
            "Operating System :: OS Independent",
            "Natural Language :: English",
                 ],
    long_description="""\
Read the docs at:

   http://pitipper.readthedocs.org

    """,
    )
