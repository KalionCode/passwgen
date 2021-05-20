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
# all possible combination leet format
import itertools

def main(fstr, config, usedKeywords):
    result = []
    possibleIndexes = [i for i in range(len(config.get('leet'))+1)]
    leetReplace = {}
    
    for n in range(1,len(config.get('leet'))):
        possibleCombosForN = itertools.combinations(config.get('leet').items(), n)
        for i in possibleCombosForN:
            a = fstr
            b = fstr
            for key, value in i:
                a = a.replace(key, value)
                b = b.replace(value, key)
            if (a != fstr and a not in result):
                 result.append(a)
            if (b != fstr and b != a and b not in result):
                 result.append(b)
    return result
                