# -*- coding: utf-8 -*-

import unittest
import os
from mathdeck import settings


class TestSettingsModule(unittest.TestCase):

    def test_opening_bogus_conf_file(self):
        path='/this/dir/does/not/exist'
        problibs = settings.ProblemLibs(path)
        with self.assertRaises(KeyError):
            problibs.get_libs()


    def test_opening_actual_conf_file(self):
        cur_dir = os.path.dirname(os.path.realpath(__file__))
        path = os.path.join(cur_dir,'fixtures','settings')
        problibs = settings.ProblemLibs(path)
        problibs.get_libs()['main']
        self.assertEqual(problibs.get_libs()['main'],'/main/dir/')

if __name__ == '__main__':
    unittest.main()
