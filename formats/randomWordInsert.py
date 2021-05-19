#random word insert format
#from passwgen/dicts
import pathlib

def main(fstr, config, usedKeywords):
    wordDictFile = pathlib.Path(__file__).parent / '../dicts/common1000.txt' 
    keywords = usedKeywords
    result = []
    with wordDictFile.open('r') as f:
        wordDict = [line.rstrip() for line in f]
    for word in wordDict: 
        for index in range(len(keywords)+1):
            keywords.insert(index, word)
            result.append(''.join(keywords))
            keywords.pop(index)
    return result
    
        
