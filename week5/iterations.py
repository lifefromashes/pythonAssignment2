import itertools
cntCombo = 0
print('Generate Combinations')
for combinations in itertools.combinations('abc', 3):
    print(combinations)
    cntCombo += 1

uniqComb = 0
print('Generate permutations')
for uniqueCombos in itertools.permutations('abc', 3):
    print(uniqueCombos)
    uniqComb += 1

cnt = 0
print("Generate Permutations")
for permutations in itertools.permutations("abcd", 4):
    print(permutations)
    cnt += 1


print("CntCombo", cntCombo)
print("UniqueCombos", uniqComb)

print("Permutations", cnt)

# print('Generate 4 permutations')
# for permutations1 in itertools.permutations('abc', 4):
#     print(permutations1)


# for variations in range(1, 4):
#     for pwTuple in itertools.combinations("abc", 3):
#         pw = ""
#         for eachChr in pwTuple:
#             pw = pw + "".join(eachChr)
#         pw = bytes(pw, 'ascii')
# rainbowList = list(permutations.items())
#
# print("Rainbow size: ", len(rainbowList), '\n')
