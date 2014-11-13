# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='mathdeck',
    version='0.0.1-planning',
    author='Patrick Spencer',
    license='BSD 3-Clause',
    url='https://github.com/patrickspencer/mathdeck',
    author_email='patrick.spencer@mail.mizzou.edu',
    description="""Mathdeck a program suite for managing the computations
                involved in writing displaying, and grading mathematical
                based homework problems.
                """,
    long_description=open('README.rst').read(),
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
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    install_requires=[
        'sympy>=0.7.5',
        'Jinja2==2.7.3',
    ]
)

