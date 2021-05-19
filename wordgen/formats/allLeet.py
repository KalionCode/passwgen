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
                