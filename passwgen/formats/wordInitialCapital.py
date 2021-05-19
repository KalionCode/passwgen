#Word-Initial capital format
def main(fstr, config, usedKeywords):
    """Word-Initial capital format"""
    result = []
    for i in usedKeywords:
        result.append(i.title())
    result = ''.join(result)
    return result