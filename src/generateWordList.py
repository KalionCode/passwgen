import itertools

import formats 
import helpers 

from helpers.registerfunc import registerfunc_init, registerfunc_getRegistered 

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
    
    # usedKeywords = []
    # depthList = [i for i in range(1, config.get('maxKeywordCombo')+1 )]
    # depth = 0
    # for i in keywords:
    #     # init d1
    #     depth += 1
    #     if (depth > config.get('maxKeywordCombo')):
    #         depth -= 1 
    #         continue
    #     usedKeywords.append(i)
    #     fstr = helpers.genfstr(usedKeywords)

    #     d1(fstr, config, usedKeywords)
    #     # Helper functions
    #     # fstr = helpers.genfstr(usedKeywords)
        
    #     # Formatter functions
    #     # helpers.printf(formats.allLeet(fstr, config, usedKeywords))
    #     # helpers.printf(formats.wordInitialCapital(fstr, config, usedKeywords))
    #     # helpers.printf(formats.randomIntInsert(fstr, config, usedKeywords))
    #     # helpers.printf(formats.specialCharInsert(fstr, config, usedKeywords))
    #     # helpers.printf(formats.randomIntComboInsert(fstr, config, usedKeywords, N ))
    #     # helpers.printf(formats.randomWordInsert(fstr,config,usedKeywords))
    #     if depth+1 not in depthList: 
    #         usedKeywords.pop()
    #         depth -=1
    #         continue
    #     for j in keywords:
            
    #         # init d2
    #         depth += 1
    #         #handle duplicates
    #         if (j in usedKeywords):
    #             depth -=1
    #             continue
    #         usedKeywords.append(j)
    #         fstr = helpers.genfstr(usedKeywords)

    #         d2(fstr, config, usedKeywords)
    #         if depth+1 not in depthList: 
    #             usedKeywords.pop()
    #             depth -=1
    #             continue
    #         for k in keywords:
    #             # init d3
    #             depth += 1

    #             # handle duplicates
    #             if (k in usedKeywords):
    #                 depth -=1
    #                 continue
    #             usedKeywords.append(k)
    #             fstr = helpers.genfstr(usedKeywords)
    #             d3(fstr, config, usedKeywords)
    #             if depth+1 not in depthList: 
    #                 usedKeywords.pop()
    #                 depth -=1
    #                 continue
    #             for e in keywords:
    #                 # init d4
    #                 depth += 1
                    
    #                 #handle duplicates
    #                 if (e in usedKeywords):
    #                     depth -=1
    #                     continue
    #                 usedKeywords.append(e)
    #                 fstr = helpers.genfstr(usedKeywords)

    #                 d4(fstr, config, usedKeywords)
    #                 # clean up d4
    #                 depth -= 1
    #                 usedKeywords.remove(e)
    #             # clean up d3
    #             depth -= 1
    #             usedKeywords.remove(k)
    #         # clean up d2
    #         depth -= 1
    #         usedKeywords.remove(j)
    #     # clean up d1
    #     depth -= 1
    #     usedKeywords.remove(i)

@registerfunc_init(config.get('maxKeywordCombo'))
@helpers.registerfunc(1)
def d1(fstr, config, usedKeywords):
    print(fstr)

def d2(fstr, config, usedKeywords):
    print(fstr)

def d3(fstr, config, usedKeywords):
    print(fstr)

def d4(fstr, config, usedKeywords):
    print(fstr)



generateWordlist(['westlake','wbhs','forrest','hill'], config=config)
