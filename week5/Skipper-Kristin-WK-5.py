'''
Skipper, Kristin
Week 5 Scripting Assignment
Date: 9/23/2022
'''
import itertools
import hashlib

rainbowTable = {}

print("Creating A Password Rainbow Table")
for variations in range(4, 8):
    for pwTuple in itertools.product("abc123&", repeat=variations):
        pw = ""
        md5Hash = hashlib.md5()
        for eachChr in pwTuple:
            pw = pw + "".join(eachChr)
        pw = bytes(pw, 'ascii')
        md5Hash.update(pw)
        md5Digest = md5Hash.hexdigest()
        rainbowTable[md5Digest] = pw

rainbowList = list(rainbowTable.items())
firstFive = rainbowList[:5]
lastFive = rainbowList[-5:]
print("Rainbow Size: ", len(rainbowTable), "\n")
print('First Five: ', firstFive)
print('Last Five: ', lastFive)


