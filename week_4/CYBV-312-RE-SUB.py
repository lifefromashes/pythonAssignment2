''' 
Regular Expression Search
Professor Hosmer
May 22
Substition Example
'''

import re

print("\nRegular Expession Substitution Example")

s = "abc %$#@ def ()**&%$% !!!@@,,,, xyz"
print(s)

txt  = re.sub('[^A-Za-z]', " ", s)

print(txt)