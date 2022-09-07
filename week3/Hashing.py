'''
Simple File Hashing Example
Professor Hosmer
August 2020
'''

import os  # Python standard library os/file system methods
import hashlib  # Python standard library hashlib
import sys  # Python standard library system specifics and functions


def hashFileContents(contents):
    sha512Obj = hashlib.sha512()
    sha512Obj.update(contents)
    hexDigest = sha512Obj.hexdigest()
    return hexDigest


while True:
    fileToHash = input("\nFile to Hash >>> ")
    if os.path.isfile(fileToHash):
        break
    else:
        print("\nInvalid File ... Please Try Again")

try:
    print("\nAttempting to hash file: ", fileToHash)

    with open(fileToHash, 'rb') as target:

        fileContents = target.read()
        digest = hashFileContents(fileContents)

        # sha512Obj = hashlib.sha512()
        # sha512Obj.update(fileContents)
        # hexDigest = sha512Obj.hexdigest()

        print("\n\n", fileToHash, " SHA-512 Hex Digest = ", digest, "\n\n")

except Exception as err:
    sys.exit("\nException: " + str(err))

print("Script Done")
