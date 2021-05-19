#leet format
def main(fstr, config, usedKeywords):
    """leet format
    - interable"""
    result = []
    fstr_leet = fstr
    for key, value in config.get('leet').items():
        a = fstr_leet.replace(key, value)
        b = fstr_leet.replace(value, key)
        if (a != fstr_leet): result.append(a)
        if (b != fstr_leet): result.append(b)
    return result