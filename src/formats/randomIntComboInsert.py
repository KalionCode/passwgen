# random int combo insert format (eg. 0043)
def main(fstr, config, usedKeywords, nDigits):
    
    result = []
    words = usedKeywords[:]
    for i in range(10**nDigits):
        stri = str(i)
        if (len(stri) < nDigits): 
            stri = stri.zfill(nDigits)
        for index in range(len(words)+1):
            words.insert(index, stri)
            result.append(''.join(words))
            words.pop(index)
    return result

