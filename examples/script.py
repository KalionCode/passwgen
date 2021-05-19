import passwgen as pgen

@pgen.utils.registerFuncU(3)
def d1(fstr, config, keywords):
    print(fstr)

pgen.generateWordList(['foo','bar'], )

