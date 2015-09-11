# -*- coding: utf-8 -*-

import unittest
import os
from tornado.testing import AsyncHTTPTestCase
from mathdeck import server

class TestHelloApp(AsyncHTTPTestCase):
    def get_app(self):
        return server.make_app()

    def test_homepage(self):
        response = self.fetch('/')
        self.assertEqual(response.code, 200)
        self.assertEqual(response.body, b'Hello, world')

if __name__ == '__main__':
    unittest.main()
