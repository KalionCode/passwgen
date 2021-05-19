import itertools

import passwgen.formats 
import passwgen.utils as utils 

from passwgen.utils.registerfunc import registerfunc_getRegistered 

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

config = {
    'maxKeywordCombo': 3,
    **default_config
}

def generateWordlist(keywords, config):
    for n in range(1,config.get('maxKeywordCombo')+1 ):
        func = registerfunc_getRegistered()[n]
        for i in itertools.product(keywords, repeat=n):
            fstr = "".join(i)
            if func is not None:
                func(fstr, config , list(i))
    
    

@utils.registerfuncU(1)
def d1(fstr, config, usedKeywords):
    print(fstr)

def d2(fstr, config, usedKeywords):
    print(fstr)

def d3(fstr, config, usedKeywords):
    print(fstr)

def d4(fstr, config, usedKeywords):
    print(fstr)



generateWordlist(['westlake','wbhs','forrest','hill'], config=config)
