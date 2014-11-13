# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='mathdeck',
    version='0.0.1-alpha',
    author='Patrick Spencer',
    license='BSD 3-Clause',
    url='https://github.com/patrickspencer/mathdeck',
    author_email='patrick.spencer@mail.mizzou.edu',
    description='Mathdeck a program suite for managing the computations'
                'involved in writing displaying, and grading mathematical'
                'based homework problems. It is written to abstract the'
                'computations so that other responsibilities such as managing'
                'users and grades can be left to more apt systems such as'
                'online course management systems.',
    long_description=open('README.rst').read(),
    zip_safe=False,
    packages=[
        'mathdeck',
        'tests',
    ],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GPL V2.0 License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    install_requires=[
        'sympy>=0.7.5',
        'Jinja2==2.7.3',
    ]
)

