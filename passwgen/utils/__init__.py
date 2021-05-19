import importlib
import os
import pathlib
from os.path import isfile, join

parentDir = os.path.dirname(__file__)
parentDirName = pathlib.Path(parentDir).stem
formats = os.listdir(parentDir)
formats = [pathlib.Path(i).stem for i in formats if (i != '__init__.py' and isfile(join(parentDir, i)))]

for i in formats:
    exec(f'{i}{parentDirName[:1].upper()} = importlib.import_module("passwgen.{parentDirName}.{i}").main')
