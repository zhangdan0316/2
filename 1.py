import re
s='  ---hello  world ***   '
#print (s.strip('-* '))

print (re.sub(r'[ *-]+','',s))
