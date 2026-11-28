import sys 
import time

def LCubS(S):
    sLen = len(S)
    best = ""

    sys.setrecursionlimit(5000)
    letterCount = {}
    for i in S:
        letterCount[i] = letterCount.get(i,0) + 1

    prunedString = ""

    for i in S:
        if(letterCount[i] >= 3):
            prunedString = prunedString + i

    globalMaxLength = sum([x // 3 for x in letterCount.values()])

    letterIndexes = {} 

    for index, letter in enumerate(prunedString):
        letterIndexes.setdefault(letter,[]).append(index)

    for letter, indexes in letterIndexes.items():
        for indexP in range(len(indexes)):
            for indexQ in range(indexP + 1, len(indexes)):

                if(len(best) == globalMaxLength):
                    return best * 3

                if(indexes[indexQ] > len(S) - 2):
                    continue

                p = indexes[indexP] + 1
                q = indexes[indexQ] + 1

                sub1 = prunedString[:p]
                sub2 = prunedString[p:q]
                sub3 = prunedString[q:]

                memTable = [[[None] * (len(sub3) + 1) for _ in range(len(sub2) + 1)] for _ in range(len(sub1) + 1)]

                def LCS(i, j, k):
                    if i == 0 or j == 0 or k == 0:
                        return ""

                    if(memTable[i][j][k] is not None):
                        return memTable[i][j][k]

                    if sub1[i - 1] == sub2[j - 1] == sub3[k - 1]:
                        r = LCS(i-1,j-1,k-1) + sub1[i - 1]

                    else:
                        r = max(
                            LCS(i - 1, j, k),
                            LCS(i, j - 1, k),
                            LCS(i, j, k - 1),
                            key=len
                        )
                    memTable[i][j][k] = r
                    return r

                LongestCommonSubsequence = LCS(len(sub1), len(sub2), len(sub3))            

                if(len(LongestCommonSubsequence) > len(best)):
                    best = LongestCommonSubsequence
    return best * 3

def LCubSTest():
    print("[--- Improved Only Stress Test (size 100) ---]")    
    improvedStart = time.perf_counter()

    output = LCubS("gFuhEsowocaoGhfiEdEwGEnFdGqbglcoDahoxuhtgttCmufkvjmBffunurjhCbnkEcCwafFdByjmBlnrqnszzqvbrpldAfwhkExn")
    print("Improved Cubic Subsequence: " + output)

    improvedEnd = time.perf_counter()

    improvedTotal = improvedEnd - improvedStart
    print("Improved Time: " + str(improvedTotal))

    print("[--- Improved Only Stress Test (size 200) ---]")    
    improvedStart = time.perf_counter()

    output = LCubS("m5jEw629S00Z3vrpTL8z0NXVm0tvGekgSE0TDRbOGm44g4R8zjhV6CDg2ReAmPv6SxbeTMgGchesIv3iriMynLTQBDJnEhulV7rZy1Ue0zmRz10C1MuMwTTrR33kESPkWahCjUQ9xVf7w3A6wesUBrxFovADDOZUGQzPDdqhBbrMJsCq2PgQ9W50VRbKTZsTYVrIJIYd")
    print("Improved Cubic Subsequence: " + output)

    improvedEnd = time.perf_counter()

    improvedTotal = improvedEnd - improvedStart
    print("Improved Time: " + str(improvedTotal))


if __name__ == "__main__":
    #LCubSTest()
    print(LCubS(input("Type a string for LCubS: ")))