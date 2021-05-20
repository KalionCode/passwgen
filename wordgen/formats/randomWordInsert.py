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
#random word insert format
#from passwgen/dicts
import pathlib

def main(fstr, config, usedKeywords):
    wordDictFile = pathlib.Path(__file__).parent / '../dicts/common1000.txt' 
    keywords = usedKeywords
    result = []
    with wordDictFile.open('r') as f:
        wordDict = [line.rstrip() for line in f]
    for word in wordDict: 
        for index in range(len(keywords)+1):
            keywords.insert(index, word)
            result.append(''.join(keywords))
            keywords.pop(index)
    return result
    
        
