

def LCubS(S):
    sLen = len(S)
    best = ""

    letterCount = {}
    for i in S:
        letterCount[i] = letterCount.get(i,0) + 1

    prunedString = ""

    for i in S:
        if(letterCount[i] >= 3):
            prunedString = prunedString + i

    for p in range(1, sLen - 1):
        for q in range(p + 1, sLen):
            sub1 = prunedString[:p]
            sub2 = prunedString[p:q]
            sub3 = prunedString[q:]

            memTable = [[[None] * (len(sub3) + 1) for _ in range(len(sub2) + 1)] for _ in range(len(sub1) + 1)]

            def LCM(i, j, k):
                if i == 0 or j == 0 or k == 0:
                    return ""

                if(memTable[i][j][k] is not None):
                    return memTable[i][j][k]

                if sub1[i - 1] == sub2[j - 1] == sub3[k - 1]:
                    r = LCM(i-1,j-1,k-1) + sub1[i - 1]

                else:
                    r = max(
                        LCM(i - 1, j, k),
                        LCM(i, j - 1, k),
                        LCM(i, j, k - 1),
                        key=len
                    )
                memTable[i][j][k] = r
                return r

            LongestCommonSubsequence = LCM(len(sub1), len(sub2), len(sub3))            

            if(len(LongestCommonSubsequence) > len(best)):
                best = LongestCommonSubsequence
    return best * 3

print(LCubS("atcgtatgcatgca"))