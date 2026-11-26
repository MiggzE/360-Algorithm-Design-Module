def LCubS(S):
    sLen = len(S)
    memo = [[[-1 for _ in range(sLen)] for _ in range(sLen)] for _ in range(sLen)]

    def findLCubS(i, j, k, string, memTable):
  
        if(i == 0 or j == 0 or k == 0):
            return 0

        if(memTable[i - 1][j - 1][k - 1] != -1):
            return memTable[i - 1][j - 1][k - 1]

        if(string[i - 1] == string[j - 1] == string[k - 1] and i != j and j != k and i != k):
            memTable[i - 1][j - 1][k - 1] = 1 + findLCubS(i - 1, j - 1, k - 1, string, memTable)
            return memTable[i - 1][j - 1][k - 1]

        memTable[i - 1][j - 1][k - 1] = max(
            findLCubS(i - 1, j, k, string, memTable),
            findLCubS(i, j - 1, k, string, memTable),
            findLCubS(i, j, k - 1, string, memTable)
        )

        return memTable[i - 1][j - 1][k - 1]

    return findLCubS(sLen, sLen, sLen, S, memo)

print(LCubS("aaa"))