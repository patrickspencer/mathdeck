# -*- coding: utf-8 -*-

"""
mathdeck.api
~~~~~~~~~~~~

This module implements the Mathdeck API.

:copyright: (c) 2014 by Patrick Spencer.
:license: BSD3, see LICENSE for more details.

"""

def display(file, seed, number):
    """Constructs and sends a :class:`Problem <Problem>`.
    Returns :class:`Problem <Problem>` object.

    :param file: method for the new :class:`Request` object.
    :param seed: Seed number to used to base random number generation off of

    Usage::

      >>> import mathdeck
      >>> output = mathdeck.display('file.py', 12345)
      Solve the following: $1+1=$<input type="text" name="ans1">
    """
    from jinja2 import Template
    template = u"""
      <htmllk>
    """
    m = Template(u"{% set a, b = 'foo', 'föö' %}")

    return file, seed, number

def check(file, seed, **kwargs):
    """Constructs and sends a :class:`Request <Request>`.
    Returns :class:`Response <Response>` object.

    :param method: method for the new :class:`Request` object.
    :param seed: Seed number to used to base random number generation off of

    Usage::

      >>> import mathdeck
      >>> output = mathdeck.display('file.py.problem', 12345)

    """

    session = sessions.Session()
    return session.request(method=method, url=url, **kwargs)
