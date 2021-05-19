import importlib
import os
import pathlib
from os.path import isfile, join

parentDir = os.path.dirname(__file__)
formats = os.listdir(parentDir)
formats = [pathlib.Path(i).stem for i in formats if (i != '__init__.py' and isfile(join(parentDir, i)))]

for i in formats:
    exec(f'{i} = importlib.import_module("formats.{i}").main')
