import itertools

import passwgen.formats 
import passwgen.utils as utils 

from passwgen.utils.registerFunc import getRegistered 

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
    
    

