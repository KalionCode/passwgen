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
import itertools

import wordgen.formats 
import wordgen.utils as utils 

from wordgen.utils.registerFunc import getRegistered 

default_config = {
    'leet':{
        'a':'@',
        'i':'1',
        'e':'3',
        't':'7',
        'o':'0',
        's':'5',
        'g':'9',
        'z':'2'
        },
    'specialChar':[i for i in ' !"#$%&\'()*+,-./:;<=>=?@[\]^_`{|}~'],
    'maxKeywordCombo':3
}

def generateWordList(keywords, config={}):
    config = {
        **config,
        **default_config
    }
    for n in range(1,config.get('maxKeywordCombo')+1 ):
        if n > len(getRegistered())-1: 
            func = None
        else: 
            func = getRegistered()[n]

        for i in itertools.product(keywords, repeat=n):
            fstr = "".join(i)
            if func is not None:
                func(fstr, config , list(i))
    
    

