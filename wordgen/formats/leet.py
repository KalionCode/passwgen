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
#leet format
def main(fstr, config, usedKeywords):
    """leet format
    - interable"""
    result = []
    fstr_leet = fstr
    for key, value in config.get('leet').items():
        a = fstr_leet.replace(key, value)
        b = fstr_leet.replace(value, key)
        if (a != fstr_leet): result.append(a)
        if (b != fstr_leet): result.append(b)
    return result