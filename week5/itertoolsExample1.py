'''
Introducing itertools
Professor Hosmer
August 2020
'''

import itertools   # Python standard library

print("Generate Combinations")
cnt = 0
for combinations in itertools.combinations("xyz", 3):
    print(combinations)

print("Generate Permuations")
for permutations in itertools.permutations("xyza", 4):
    print(permutations)
    cnt+=1

print(cnt)    
print("Generate Product")
cnt = 0
for variations in range(4,8):
    for products in itertools.product("xyza", repeat=variations):
        print(products)    
        cnt+=1
print("Product Count: ", cnt)