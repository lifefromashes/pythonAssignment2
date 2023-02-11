# print(3 + 4 == 7)
# print(3 / 4)
# print("a string", "xyz")
# print(16 - 2 * 5 // 3 + 1)
# print("""This message input has
# several lines
# of the text.""")
#
# print(-3.999, int(-3.999))

# print("123.45")
# print(float("123.45"))
# print(type("123.45"))
# print(type(float("123.45")))

# def square(x):
#     runningtotal = 0
#     for counter in range(x):
#         runningtotal = runningtotal + x
#     return runningtotal
# n = 15
# result = square(n)
# print(result)

#
# import random
#
# diceThrow = random.randrange(1, 7)
# print(diceThrow)

# def f1(x):
#     for counter in range(x):
#         runningtotal = 0
#         runningtotal = runningtotal + x
#     return runningtotal
#
# def f2(x):
#     runningtotal = 0
#     for counter in range(x):
#         runningtotal = runningtotal + x
#
#     return runningtotal
#
# toSquare = 10
# f1Result = f1(toSquare)
# f2Result = f2(toSquare)
# print(f1Result, f2Result)

def removeSomeChars(s):
    vowels = "aeiouAEIOU"
    digits = "0123456789"
    newS = ""
    for eachChar in s:
        if (eachChar not in vowels) and (eachChar not in digits):
            newS = newS + eachChar
    return newS


print(removeSomeChars("APCV320"))
