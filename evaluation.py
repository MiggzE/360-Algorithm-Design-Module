import LCubS_Baseline
import LCubS_Improved
import time
def compareImplementations(string):
    baselineStart = time.perf_counter()

    output = LCubS_Baseline.LCubS(string)
    print("Baseline Cubic Subsequence: " + output)

    baselineEnd = time.perf_counter()

    baselineTotal = baselineEnd - baselineStart

    print("Baseline Time: " + str(baselineTotal))

    improvedStart = time.perf_counter()

    output = LCubS_Improved.LCubS(string)
    print("Improved Cubic Subsequence: " + output)

    improvedEnd = time.perf_counter()

    improvedTotal = improvedEnd - improvedStart

    percentDiff = round(baselineTotal / improvedTotal)

    print("Improved Time: " + str(improvedTotal))
    print("Improved Algorithm is around " + str(percentDiff) + "x faster")

print("[--- Basic String Test ---]")
compareImplementations("atcgtatgcatgca")

print("[--- Pruning Check Size 20 ---]")
compareImplementations("aRaaRKbaac6bDacaaccb")

print("[--- Pruning Check Size 25 ---]")
compareImplementations("cacbXbabIacaDYT8aacaababc")

print("[--- Early Stop Size 20 ---]")

print("[--- Early Stop Size 25 ---]")
compareImplementations("bacccXacabacccacabacccaca")

print("[--- Strategic Slicing Size 20 ---]")
compareImplementations("ggcaagatggttaatcaaga")

print("[--- Strategic Slicing Size 25 ---]")
compareImplementations("tacttgagtggcgtacaactaccag")

print("[--- Varied Length 1 (Size 15) ---]")
compareImplementations("adacbdeddaeadae")

print("[--- Varied Length 2 (Size 20) ---]")
compareImplementations("abbeefabaffebcbdcada")

print("[--- Varied Length 3 (Size 25) ---]")
compareImplementations("ebeaacaecfbbgcfcebbdcbbaf")

print("[--- Varied Length 4 (Size 30) ---]")
compareImplementations("ccgibfadgjhacgbgdeejaffahhbfhh")
