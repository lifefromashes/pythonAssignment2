'''
Simple Rainbow Table Construction 
using, a dictionary
'''
import itertools
import hashlib

rainbowTable = {}

print("Create Password Rainbow Table")
for variations in range(4, 7):
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

# for hashValue, pwValue in rainbowTable.items():
# for hashValue, pwValue in rainbowList:
#     print('First Five: ', firstFive)
# print(hashValue, pwValue)

# print first five and last five:
# firstFive = list(rainbowTable.items())[:5]
# lastFive = list(rainbowTable.items())[5:]
#
# sampleList = firstFive + lastFive
# print('sample list: ', sampleList)
#
# #print w/hashes
# print('{:<40s}'.format("HASH"), "Password")
# print('=' * 60)
# for eachEntry in sampleList:
#     hash = eachEntry[0]
#     pw = eachEntry[1]
#     print('{:<40s'.format(hash), pw)
