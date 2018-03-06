import re
data = open('text.txt').read()
#print (data)
res = re.sub('(\w{3}) (\d{2}) (\d{2}) (\d{4})',r'\4/\2/\3/\1',data)
print res