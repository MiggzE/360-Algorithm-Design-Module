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

    start = time.perf_counter()

    output = LCubS_Improved.LCubS(string)
    print("Improved Cubic Subsequence: " + output)

    end = time.perf_counter()

    total = end - start

    print("Improved Time: " + str(total))

print("[--- Basic String Test ---]")
compareImplementations("atcgtatgcatgca")

print("[--- Pruning Check 1 ---]")
compareImplementations("mississippi")

print("[--- Pruning Check 2 ---]")
compareImplementations("aabbccddeeffgg")

print("[--- Multiple LCubS 1 ---]")
compareImplementations("ccbbcbcbcb")

print("[--- Multiple LCubs 2 ---]")
compareImplementations("cbabaccbcbc")

print("[--- Strategic Slicing 1 ---]")
compareImplementations("abcdefgabcdefgabcdefg")

print("[--- Strategic Slicing 2 ---]")
compareImplementations("abcdefghabcdefghabcdefgh")

print("[--- Varied Length 1 (Size 15) ---]")
compareImplementations("adacbdeddaeadae")

print("[--- Varied Length 2 (Size 20) ---]")
compareImplementations("abbeefabaffebcbdcada")

print("[--- Varied Length 2 (Size 25) ---]")
compareImplementations("ebeaacaecfbbgcfcebbdcbbaf")

print("[--- Varied Length 2 (Size 30) ---]")
compareImplementations("ccgibfadgjhacgbgdeejaffahhbfhh")
