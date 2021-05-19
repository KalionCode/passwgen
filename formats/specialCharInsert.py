# insert special char format
def main(fstr, config, usedKeywords):
    """insert special char format
    - interable"""
    result = []
    words = usedKeywords[:]
    for i in config.get('specialChar'):
        for index in range(len(words)+1):
            words.insert(index, i)
            result.append(''.join(words))
            words.pop(index)
    return result