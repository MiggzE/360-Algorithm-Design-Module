def isCubic(string):
    if len(string) % 3 != 0:
        return False
    cSequenceLen = len(string) // 3
    return string[:cSequenceLen] == string[cSequenceLen:cSequenceLen * 2] == string[cSequenceLen * 2:]

def LCubS(S):
    pass

print(isCubic("ababab"))