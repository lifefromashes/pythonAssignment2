''' 
Regular Expression Simple Email
Professor Hosmer
May 22
Find Email
'''

import re

print("\nRegular Expession Email Pattern Example")
emailPattern    = re.compile(b'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,3}')  


s = b"This is a test ChesterHosmer@arizona.edu  a bunch of other words sundar@google.com more wordsjeff@amazon.com more words"
print(s)

emailList = emailPattern.findall(s)
print(emailList)

