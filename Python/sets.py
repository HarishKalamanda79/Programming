#set's
s = {} #by defult dictionary
print("Default {} type: ",type(s))

Set = {4,6,2}
print("Values only {} type: ",type(Set))

set1 = {2,6,3,9,1,9,2,24,3,7,6,9,2,3}
print("Printing set with removing duplicate's: ",set1)#it print's with removing duplicate's

'''
.add()
.update()
.pop()
.remove()
'''

#.add()
set2 = {2,4,19,20,24}
set2.add(32) #Adding 32 into set2 variable
print(set2)

#.update() => update({})
set2.update({33,40,41,42}) #adding bulk amount of data, here we use {} sample => .update({_,_,_,_})

print("printing set after .update():",set2)

#.pop()
set2.pop() #randomly delating one data in set2
print("Randomly delate date using .pop():",set2)

#.remove()
set2.remove(4) #removig partivular value in set2
print(set2)

#set operation's
'''
union
intersection
difference
is subset
is superset
'''

#.union()
a = {1,2,3,4,5,6}
b = {3,4,6}
print("union of a & b:",a.union(b)) #adding a+b set's, and removing duplicate's on that and then print's

#.intersection()
print("intersection of a & b:",a.intersection(b)) #printing same values from both a & b set's

#.difference()
print("Difference between a and b: ",a.difference(b)) #print's a value's, difference in b value's

#.issubset()
print(a.issubset(b)) #here a is superset not subset so: False
