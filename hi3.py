import re
mystr='''My name is Hasaan.My registration number is L1F21BSCS1057.My gmail is L1F21BSCS1057@gmail.com
 and L1F21BSCS1057@ucp.edu.pk and contact no is 0203-2345672.'''
patt= re.compile(r'\d{4}-\d{7}')
matches = re.finditer(mystr)
for match in matches:
    print(match)