import wordgen as wgen

@wgen.utils.registerFuncU(3)
def d1(fstr, config, keywords):
    print(fstr)

wgen.generateWordList(['foo','bar'], )

