a, b, c= 2, 4, "ima"
print(a, b, c)

type(a) #check the dataType of the variable

#u can check whether given 2 variables contains similar values or different 
#values by using ^ xor operator
a = True
b = False
c = a ^ b
print(c)

y = 2
y += 2
print(y)
                #getting inputs----------------------------------------------------------------------------------------
#how to take user inputs without hard coding
print("enter your name: ")
name = input()
print("Hello"+name) #this will concatanate the 2 strings to a one string
print("Hello",name) #this will print 2 strings one after the other with a space in the middle

#to avoid input statement going to the 2nd line, write as below
print("enter your name: ", end="")
name = input() 
print("\n")
                #Lists--------------------------------------------------------------------------------------------------
#lists in python
TestList = [234,889,223,200]

#add a new item to the list
TestList.append(40)
print(TestList)

#remove a specific item that u mention from the list
TestList.remove(889)
print(TestList)

#remove an item calling its index
TestList.pop(0)
print(TestList)

#u can add 2 lists to make a one list
x = [33,88,99,22]
y = [3, 8, 9, 2]
c = x + y
print(c, "\n")

#u can even check whether a item is existing in your list
print( 88 in x)
print ( 88 not in x, "\n")

               #Dictionary-------------------------------------------------------------------------------------------------

#create a Dictionary of set of data sets where each data set 
#contains a KEY and VALUE
Dic = {'1200' : "colombo", '1300': "Gampaha"}
print(Dic, "\n")
#add more data sets to our dictionary
Dic['1400'] = "matara"
print(Dic, "\n")
#can get only the keys of all the data sets
print(Dic.keys(), "\n")
#can get only the values of all the data sets
print(Dic.values(), "\n")
#can get the value calling a specific key of the list
print(Dic['1400'],"\n")

#u can even put complex set of data instead of 1 value of a key
Dic['newKeyForCities'] = {'colombo','matara','dikwella'}
print(Dic, "\n")

#use get(<key>,<defaultValue>) function to check whether there's a value to this key
#if there's no such key then return a default value
x = Dic.get('1400', 0)
print(x, "\n")

#delete data sets in a dictionary
del Dic['1200']
print(Dic, "\n")
#use clear funtion to delete the whole dictionary
Dic.clear()
print(Dic, "\n")

#dictionaries can be very complex (with many sub dics like branches of a tree)
x = { "a": ["hi", "hello", "good morning"],
      "b": ["bye", "good night"],
      "c": 16
    }
print(x)
#if u append something new to one of those a/b, it will be automatically
# added to the original dictionary as well. 
y = x["a"] #because now this y becomes a pointer to that dic
y.append("all good")
print(x)
                  
                   #sets (kulaka)-----------------------------------------------------------------------------------------

setA = {"colombo", "matara", "kandy"}#in a set there's no key-value pairs like in dictionaries
setB = {"kegalle", "akuressa", "kandy"}
#set has only the keys. as in mathematic sets, there can't be duplicate values in one set
#****no duplicate values in sets, the order of items in the output can be varied
#so we can't access the items in a set calling indexes or element wise(ex: y = setA("matara"))
setA.add("matara")#this will not be added to the set again
setA.add("gampaha")#this will be added

#2 sets can be added from Union function or from pipe(|) but cannot add by + mark
x = setA.union(setB)
print(x)
#2 sets can be substracted as well
x = setA - setB
print(x) #answer will be: colombo, matara

#we can just find whether any element is existing in the set or not
print("matara" in setA)

                     #tuples------------------------------------------------------------------------------------------------

#if u have a data set of different types of data(similar to a tuple in a DB table),
#then u can easily group into a one element(a tuple) as below
# but the disadvntge is, that u cannot remove any item inside a tuple which u've created
#but u can access any of them seperately through the index

praneethDetails = ("Praneeth", 26, "SriLanka", "Germany", "Praneeth")
print(praneethDetails)
#access items
print( praneethDetails[0]) #this will output the name 'praneeth'
#can also count the no of similar values are existing in the tuple
noOfItems =  praneethDetails.count("Praneeth")
print("No of 'praneeth' words: "+ str(noOfItems))
#can assign all those items in a tuple to new variables
name, age, country, residence, nextName = praneethDetails
print(name)
print(age)
print(country)
#when u've created a Tuple, u can't delete any item in that tuple dirrectly. if u want then u'll have to convert it to a List and then delete

                                        #Slicing data in a List/tuple/String-------------------------------------------------------

#data in a list can be easily extracted to a new variable easily by sending the 2 parameters(starting index, ending index of the data range that u want)
listX = ['a', 'b', 'c', 'd']
slicedData = listX[1:7] #this will extract all the data from 0 to end (1,2,3)
slicedData2 = listX[0:-1] #last index will be ignored (output- 0,1,2)
print(slicedData)
print(slicedData2)

#similarly we can slice characters in a string as well
s1 = "Hello world"
x = s1[ 0 : -1] #this will ignore the last char in the string
print(x)
print("character in index 3: "+ x[3]) #u can also get a one char in the string by calling its index like this
