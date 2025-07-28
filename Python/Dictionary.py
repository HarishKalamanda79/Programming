# Dictionary Not works indexing
dic = {2:'xyz', 24:'Harish', 'star':5}
print("Printing Dictionary: ",dic)

print(dic[24])#printing Value of 24

'''
Methods
1) get()
2) update()
3) values()
4) keys()
5) items()
'''

#get()
a = dic.get(24)#getting 24 value in to a variable
print(a)#printing a Variable

#values()
print("Values:",dic.values())#converting into list and print value's only

#keys()
print("Key's:",dic.keys())#Converting into list and print key's only

#items()
print("Printing Both Item's: ",dic.items()) #converting to list and printing Keys with Values, {items}.

#update()
print(dic.update({32:'santhu'})) #one key with a value updated, and we can store it in a variable also
print("Printing Dictionary: ",dic)

for i in dic: #here we accessing key's olny, follow 👇🏻
    print(i)

for i in dic.items(): #Here we accessing items {keys : values} using => .items() we can use .values() keys are default.
    print(i)

for i in {2:'xyz', 24:'Harish', 'star':5}:
    print(i)

#same as 👆🏻.

for i,j in {2:'xyz', 24:'Harish', 'star':5}.items(): #here we accessin items in to i,j Variables
    print(i,j) #printing i,j Values
    
 