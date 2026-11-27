def LCubS(S):
    sLen = len(S)
    best = ""
    
    for p in range(1, sLen - 1):
        for q in range(p + 1, sLen):
            sub1 = S[:p]
            sub2 = S[p:q]
            sub3 = S[q:]

            memTable = [[[-1] * (len(sub3) + 1) for _ in range(len(sub2) + 1)] for _ in range(len(sub1) + 1)]

            def LCM(i, j, k, string, memo):
                if i == 0 or j == 0 or k == 0:
                    return 0

                if(memTable[i][j][k] != -1):
                    return memTable[i][j][k]

                if sub1[i - 1] == sub2[j - 1] == sub3[k - 1]:
                    r = 1 + LCM(i-1,j-1,k-1)

                else:
                    r = max(
                        LCM(i - 1, j, k)
                        LCM(i, j - 1, k)
                        LCM(i, j, k - 1)
                    )
                memTable[i][j][k] = r
                return r
        

print(LCubS("aaaa"))