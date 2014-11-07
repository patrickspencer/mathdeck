import os
import sys

target_dir = os.path.dirname(os.path.realpath(__file__))
target_file =  os.path.join(target_dir, "hello.py")

if sys.version_info[0] == 2:
    import imp
    problem = imp.load_source('hello',target_file)

print problem.NewClass()

if sys.version_info[0] == 3:
    import importlib.machinery
    loader = importlib.machinery.SourceFileLoader("hello.py", target_dir)
    foo = loader.load_module()


