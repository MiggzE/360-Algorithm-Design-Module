import LCubS_Baseline
import LCubS_Improved
import time

start = time.perf_counter()

LCubS_Baseline.LCubS("atcgtatgcatgca")

end = time.perf_counter()

total = end - start

print("Baseline Time: " + str(total))

#-----------------------------------------------------#

start = time.perf_counter()

LCubS_Improved.LCubS("atcgtatgcatgca")

end = time.perf_counter()

total = end - start

print("Improved Time: " + str(total))

