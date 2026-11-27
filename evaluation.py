import LCubS_Baseline
import LCubS_Improved
import time
def compareImplementations(string):
    start = time.perf_counter()

    output = LCubS_Baseline.LCubS(string)
    print("Baseline Cubic Subsequence: " + output)

    end = time.perf_counter()

    total = end - start

    print("Baseline Time: " + str(total))

    print("#-----------------------------------------------------#")

    start = time.perf_counter()

    output = LCubS_Improved.LCubS(string)
    print("Improved Cubic Subsequence: " + output)

    end = time.perf_counter()

    total = end - start

    print("Improved Time: " + str(total))

print("[--- Basic String Test ---]")
compareImplementations("atcgtatgcatgca")
