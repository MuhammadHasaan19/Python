import re
mystr='''My name is Hasaan.My registration number is L1F21BSCS1057.My gmail is L1F21BSCS1057@gmail.com
 and L1F21BSCS1057@ucp.edu.pk and contact no is 0203-2345672.'''
patt= re.compile(r'\d{4}-\d{7}')
matches = re.finditer(mystr)
for match in matches:
    print(match)

import re
mystr='''My name is Hasaan.My registration number is L1F21BSCS1057.My gmail is L1F21BSCS1057@gmail.com
 and L1F21BSCS1057@ucp.edu.pk and contact no is 0203-2345672.'''
#--------(1) 1.	Match a valid email address. (l1f20bscs0001@ucp.edu.pk)
patt= re.compile(r'^[A-Z|a-z|0-9]@[A-Z|a-z|0-9]+\.+[a-z]')
matches = patt.finditer(mystr)
for match in matches:
    print(match)

#--------(2) 2.	Extract all the URLs from a given text.
patt = re.findall("\w", mystr)

print(patt)

if patt:
  print("Yes, there is a match!")
else:
  print("No match")

#--------(3) 
patt= re.compile(r'\d{4}-\d{7}')
matches = re.finditer(mystr)
for match in matches:
    print(match)

#3jgtgs
mystr='''My name is Hasaan.My registration number is L1F21BSCS1057.My gmail is hasaan230@gmail.com
 and L1F21BSCS1057@ucp.edu.pk.My contact no is 0203-2345672.This is URL  https://www.coderHack.org/'''
my_str = "Hi my name is John and email address is john.doe@somecompany.co.uk and my friend's email is jane_doe124@gmail.com"
emails = re.findall("([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)", my_str)

for mail in an email:
print(mail)
