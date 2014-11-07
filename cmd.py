# -*- coding: utf-8 -*-

import os
import sys
import argparse
from mathdeck import parse


sys.dont_write_bytecode = True

LIBRARY_DIR = os.path.abspath(os.path.join(
        os.path.dirname( __file__   ), '..', 'problem-library'))

parser = argparse.ArgumentParser(
                description='Process mathdeck problem file into html.')
parser.add_argument('file', type=str, help='input problem file')

args = parser.parse_args()
FILE_SOURCE = os.path.join(LIBRARY_DIR,args.file)
print FILE_SOURCE
