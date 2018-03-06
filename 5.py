list = ['Google', 'Runoob', 1997, 2000]
list2 = [1,2,3,1]
print ("the third is:",list[2])
list[2]=2001
print ("the new third is:",list[2])
del list[2]
print list
print len(list)
list3 = list + list2
print list3
list4 = list2*2
print list4
print max(list2)
print min(list2)
list2.append(4)
print list2
a = list2.count(1)
print a
list2.extend(list)
print list2
b = list2.index(2000)
print b
list2.insert(0,'hello')
print list2
list2.pop()
print list2
list2.remove(1)
print list2
list2.sort(reverse=True)
print list2
list2.sort(reverse=False)
print list2
print (r'\n')
print ('\n')
print (r'\n')