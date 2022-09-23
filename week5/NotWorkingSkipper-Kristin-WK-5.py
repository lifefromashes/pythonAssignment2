import itertools
import hashlib

from week5.itertoolsExample1 import variations



rainbowTable = {}  # create an empty dictionary

print('Create Simple Rainbow Table')
for variation in range(3, 5):
    for pwTuple in itertools.product('xyz', repeat=variations):
        pw = ''
        md5Hash = hashlib.md5()

        for eachChar in pwTuple:
            pw = pw + ''.join(eachChar)

            pw = bytes(pw, 'ascii')
            md5Hash.update(pw)

            md5Digest = md5Hash.hexdigest()
            rainbowTable[md5Digest] = pw

        for hashValue, pwValue in rainbowTable.items():
            print(hashValue, pwValue)


#print first five and last five:
firstFive = list(rainbowTable.items())[:5]
lastFive = list(rainbowTable.items())[5:]

sampleList = firstFive + lastFive
print('sample list: ', sampleList)

#print w/hashes
print('{:<40s}'.format("HASH"), "Password")
print('=' * 60)
for eachEntry in sampleList:
    hash = eachEntry[0]
    pw = eachEntry[1]
    print('{:<40s'.format(hash), pw)