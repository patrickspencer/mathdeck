# -*- coding: utf-8 -*-

from codecs import open

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open('README.rst', 'r', 'utf-8') as f:
    readme = f.read()
with open('HISTORY.rst', 'r', 'utf-8') as f:
    history = f.read()
with open('AUTHORS.rst', 'r', 'utf-8') as f:
    authors = f.read()

setup(
    name='mathdeck',
    version='0.0.1-planning',
    author='Patrick Spencer',
    license='Apache 2.0',
    url='https://github.com/patrickspencer/mathdeck',
    author_email='patrick.spencer@mail.mizzou.edu',
    description="""Mathdeck a program suite for managing the computations
                involved in writing displaying, and grading mathematical
                based homework problems.
                """,
    long_description=(readme + '\n\n' +
                      history + '\n\n' +
                      authors),
    zip_safe=False,
    packages=[
        'mathdeck',
        'tests',
    ],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Console',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    install_requires=[
        'sympy>=0.7.5',
        'Jinja2==2.7.3',
    ]
)

