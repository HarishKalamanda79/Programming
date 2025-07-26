'''
this is multi-line comment in python
'''
#this is single line comment in python

#Strings
'''
single line quotes ('')
double line quotes ("")
triple line quotes(''' ''' (or)""" """)
'''

#String metods
#.lower()
string = "HELLO WORLD!"
string = string.lower()#string variable value convert into lower case and store again into string1 variable
print("Converting to Lower-Case: ",string)#Printing String

#.upper()
string = string.upper()
print("Converting to Upper-Case: ",string)

#endswith()
print('''String ends with "WORLD!", : ''',string.endswith("WORLD!"))

#startswith()
print('''String Starting with "HELLO", :''' ,string.startswith("HELLO,"))

#replace()
string = string.replace("WORLD!","HARISH!")
print("Replacing WORLD with my name: ",string)

#split()
List = string.split()
print("Those strings are split and store list: ",List)

#removeprefix()
string1 = "Startingprefix Endingsuffix"
print('''removeing "Startingprefix": ''',string1.removeprefix("Startingprefix"))
#removesuffix()
print('''removeing "Endingsuffix": ''',string1.removesuffix("Endingsuffix"))

#index()
nm = "Harish Rao"
print("Printing Rao index number: ",nm.index("Rao"))

#find()
print("finding Rao's indexing number: ",nm.find("Rao"))
'''.find() is same as .index(), But You enter Wrong string it will shows output: -1 and .index() shows error'''

#count()
print("How many times returned 'a' in my name: ",nm.count("a"))

st = "    strip Value    "
print("Removing spaces Before the word and After the Word, But not in Middle:",st.strip())

#rstrip()
print("removing Right side Spaces:",st.rstrip())

#lstrip()
print("removing Left side Spaces:",st.lstrip())

#List[ ] methods

li = [2,3.14,"Harish",True,7.3,"Nani",2,False,"Kumar",7.3,24]

#.append()
li.append("sunny")
print('''Printing after appending "sunny": ''',li)

#.extend()
li.extend(["santhu",143,"sai",9177,9.9,])
print('printing after extending list: ',li)

#.remove()
li.remove(9177)
print("printing List After removeing a number:",li)

#.pop()
li.pop(-3)
print("Removeing by the index value: ",li)

#.count()
print("Counting the repeted number: ",li.count(7.3))

#.index()
print("Finding index value of My name: ",li.index("Harish"))

#.insert()
li.insert(2,"love")
print("printing love in the index value of 2: ",li)

#[Start : Stop : Skip] => list Slicing
print("Printing [start : stop : Skip] =>",li[0:10:2])