#Random-number append format 
def main(fstr, config, usedKeywords):
    """Random-number append format 
    - interable"""
    result = []
    words = usedKeywords[:]
    for i in range(10000):
        for index in range(len(words)+1):
            words.insert(index, str(i))
            result.append(''.join(words))
            words.pop(index)
    return result

