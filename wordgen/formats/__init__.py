# Copyright 2021 Alex Zhao
#
# This file is part of WordGen.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, see <http://www.gnu.org/licenses/>.
import importlib
import os
import pathlib
from os.path import isfile, join

parentDir = os.path.dirname(__file__)
parentDirName = pathlib.Path(parentDir).stem
formats = os.listdir(parentDir)
formats = [pathlib.Path(i).stem for i in formats if (i != '__init__.py' and isfile(join(parentDir, i)))]

for i in formats:
    exec(f'{i}{parentDirName[:1].upper()} = importlib.import_module("wordgen.{parentDirName}.{i}").main')
