#tuple
t = (24, 5, "harish", 3.14, True, "sunny", False)
print(type(t))
print("Tuple: ",t)

print("2nd indexing value:",t[2])

print("0 start : 6 stop : 2 skip",t[0:6:2])#6th index value will be excluded
'''(start : stop : skip) => print's first value than 0+2=2 skip's 2nd value, 2+2=4 skip's 4th value 4+2=6, end value also 6 so, 6th value is excluded'''

#min, max, sum & len.
t1 = (5,6,2,7,12,24,1,32,4)
print("Minium value:",min(t1))#printing min value
print("Maximum value:",max(t1))#printing max value
print("Sum of all:",sum(t1))#Sum of all
print("Lenth of t1:",len(t1))#printing length

#concatenation 
t2 = (2,5,6)
t3 = (4,8,9)
print("Concatenation of t2+t3: ",t2+t3) #concatenating

#repetition
a = (2,4,6)
print("Repeting 3 time's of a: ",a*3) #repeting and printing 

#iteration
for i in a:
    print(i) #iterating and printing one by one

# Membership operator's "in, not in"
print("6 in t1: ",6 in t1)
print("6 not in t1: ",6 not in t1)

#identify operator's {is, is not}
print("t2 is t3:",t2 is t3)
print("t2 is not t3:",t2 is not t3)


