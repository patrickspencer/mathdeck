# -*- coding: utf-8 -*-

import unittest
import os
from mathdeck import settings


class TestSettingsModule(unittest.TestCase):

    def test_opening_conf_file(self):
        cur_dir = os.path.dirname(os.path.realpath(__file__))
        problibs = settings.ProblemLibs()
        test_settings = os.path.join(cur_dir, 'fixtures', 'settings', 'testsettings.json')
        lib_name = problibs.get_dir(settings_file = test_settings)
        self.assertEqual(lib_name, '/main/lib/dir/')

    def test_opening_alt_conf_file(self):
        cur_dir = os.path.dirname(os.path.realpath(__file__))
        problibs = settings.ProblemLibs()
        test_settings = os.path.join(cur_dir, 'fixtures', 'settings', 'testsettings.json')
        lib_name = problibs.get_dir(settings_file = test_settings, lib_name = "alt_lib")
        self.assertEqual(lib_name, '/another/problem/lib/dir/')

    def test_opening_real_conf(self):
        problibs = settings.ProblemLibs()
        test_settings = os.path.join(cur_dir, 'fixtures', 'settings', 'testsettings.json')
        lib_name = problibs.get_dir(settings_file = test_settings)

if __name__ == '__main__':
    unittest.main()
