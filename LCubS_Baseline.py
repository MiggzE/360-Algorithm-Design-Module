def isCubic(string):
    if len(string) % 3 != 0:
        return False
    cSequenceLen = len(string) // 3
    return string[:cSequenceLen] == string[cSequenceLen:cSequenceLen * 2] == string[cSequenceLen * 2:]

def LCubS(s):
    def findLCubS(i , curr):
        if i == len(s):
            if isCubic(curr):
                return curr
            else:
                return ""
        addCurrLetter = findLCubS(i + 1, curr + s[i])
        skipCurrLetter = findLCubS(i + 1, curr)
        return max(addCurrLetter,skipCurrLetter,key=len)
    return findLCubS(0,"")


print(LCubS("aaaa"))