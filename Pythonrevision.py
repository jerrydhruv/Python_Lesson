"""Varibles & data types."""
# ("Dhruv Sharma")

# print("Dhruv Sharma is my name .")
# print("My age is 19 years old .")

# print("Dhruv Sharma is my name .", " My age is 19 years old .")
# print(22)
# print(22+33+34+10)

# name1 = "Dhruv Sharma"
# name2 = "Devidson"
# print("name2")
# print("name1")

# name = "Dhruv Sharma"
# age = 19
# price = 22.99

# print(type(name))
# print(type(age))
# print(type(price))

# name1 = "dhruv"
# name2 = 'dharv'
# name3 = '''dhruv'''

# print(name1)
# print(name2)
# print(name3)

# age = 19
# old = False
# a = None
# print(type(old))
# print(type(a))

# a = 2 
# b = 8 
# sum = a+b 
# print(sum)

# a = 296
# b = 88 
# diff = a-b
# print(diff)

# name = input("name:")
# age = int(input("age:"))
# price = float(input("price:"))

# print("My name is", name, "and I am",age,"years old")

# light = print("light :")
# if(light == "red"):
#     print("stop")
# elif(light == "green"):
#     print("go")
# elif(light == "yellow"):
#     print("look")
# else:
#     print("light is brooken")

# grade = print("grade :")
# if(grade == "A"):
#     print("exelent")
# elif(grade == "B"):
#     print("good")
# elif(grade == "C"):
#     print("average")
# else:
#     print("bad")

# marks = input("marks :")
# marks = int(marks)

# if(marks >= 90):
#     print("A")

# elif(marks >= 80 and marks < 90):
#     print("B")
# elif(marks >= 70 and marks < 80):
#     print("C")

# else:
#     print("D")

# a = 595
# b = 286
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a%b)
# print(a**b)

# a = 50
# b = 20
# print(a == b)
# print(a != b)
# print(a >= b)
# print(a > b)
# print(a <= b)
# print(a < b)

# num = 10
# num = num + 10
# print("num :", num)

# num = 10 
# num += 10
# print("num :", num)

# num = 10
# num -= 10
# print("num :", num)

# num = 10
# num *= 5
# print("num :", num)

# num = 10
# num /= 5
# print("num :", num)

# num = 10
# num %= 5
# print("num :", num)

# num = 10
# num //= 5
# print("num :", num)

# num = 10
# num **= 5
# print("num :", num)

# a = 50
# b = 30
# print(not False)
# print(not True)
# print(not (a>b))

# val1 = False
# val2 = True
# print("AND operator:", val1 and val2)
# print("OR operator:", val1 and val2)
# print("OR operator:", (a == b) or (a > b))

# a = 2
# b = 4.25
# sum = a+ b 
# print(sum)

# a = int("2")
# b = 4.25
# print(type(a))
# print(a + b)

# a = 3.14
# a = int(a)
# print(type(a))

# name = input("enter your name :")
# print("welcome", name)

# name = input("enter your age:")
# print("you enterd", name)

# val = input("enter some value:")
# print(type(val),val)

# val = print("enter some value:")
# print(type(val),val)

# int("5")
# val = float(input("enter some value:"))
# print(type(val),val)

# name = input("enter your name:")
# age = int(input("enter age:"))
# marks = float(input("enter marks:"))
# print("welcome=", name)
# print("age=", age)
# print("marks=", marks)

"""Chapter Second: Strings & Conditional Statements"""

# str1 = "This is a string."
# str2 = 'Jerryclub'
# str3 = """This is a multiline string"""
# "This is Jerrysclub Tutorial of Python"

# str1 = "This is a string. we are creating it in python"
# print(str1)

# str2 = "This is a string.\nwe are creating it in python"
# print(str2)

# str3 = "This is a string.\twe are creating it in python"
# print(str3)

# str1 = "Inter"
# str2 = "shala"
# finL_str = str1+str2
# print(finL_str)

# str1 = "Inter"
# len1 = len(str1)
# print(len1)
# str2 = "shala"
# len2 = len(str2)
# print(len2)
# final_str = str1+" "+str2
# print(final_str)
# print(len(final_str))

"""Indexing"""
# str = "jer ry"
# ch = str[2]
# print(ch)

# str = "jer ry"
# ch = str[3]

"""Slicing"""
# str = "Jerry"
# print(str[1:4])

# str = "Samsung"
# print(str[4:len(str)])

# str = "Intershala"
# print(str[:3])
# print(str[5:])

# str = "Intershala"
# print(str[-4:-1])
# print(str[-3:-2])

"""String Functons"""

# str = " I am studying python from Apnacollege"
# print(str.endswith("ege"))

# str = " I am studying pyhton from Jerryclub"
# str = str.capitalize()
# print(str)

# str = " I am studying python from Intershala"
# print(str.replace("python", "ruby"))

# str = " I am studying python from Udemy"
# print(str.find("a"))

# str = "I am studying python from Apnacollege"
# print(str.count("am"))

"""Q1, Write a program to input user's first name & print it's lenght."""

# name = input("Enter your name :")
# print("length of your name is :", len(name))

"""Q2, Write a program to find the occurrence of '$' in a string."""

# name = input("Enter your name :")
# print("Occurrence of '$' in your name is :", name.count("$"))

"""Q2, Write a program to find the occurrence of '$' in a string. """

# str = "Hi, $ I am $ symbol $99.99"
# print(str.count("$"))

"""Conditional Statements
#if-elif-else(SYNTAX)"""

# light = "green"

# if(light == "red"):
#     print("stop")
# elif(light == "green"):
#     print("go")
# elif(light == "yellow"):
#     print("look")
# else:
#     print("light is broken")

# num = 5

# if(num > 2):
#     print("num is greater than 2")
# elif(num >3):
#     print("num is greater than 3")
# else:
#     print("num is less than 2")

# marks = int(input("enter students marks : "))

# if(marks >= 90):
#     grade = "A"
# elif(marks >= 80 and marks >= 90):
#     grade = "B"
# elif(marks >= 70 and marks >= 80):
#     grade = "C"
# else:
#     grade = "D"

# print("grade of the students -= ", grade)

"""nesting"""
# age = 98

# #nesting
# if(age >= 18):
#     if(age >= 80):
#         print("cannot drive")
#     else:
#         print("can drive")
# else:
#     print("cannot drive")

"""Let's Practice Q&A.
Q1, Write a programme to check if a number entered by the user is odd or even."""

# num = int(input("Enter a number :"))
# if(num % 2 == 0):
#     print(num, "is an even number") 
# else:
#     print("ODD")

"""Q2, write a programme to finde the greatest of 3 number by the user."""

# a = int(input("Enter first number :"))
# b = int(input("Enter second number :"))
# c = int(input("Enter third number :"))

# if(a > b and a > c):
#     print(a, "is greater")
# elif(b > a and b > c):
#     print(b, "is greater")
# else:
#     print(c, "is greater")

"""Q3, Write a pogramme to check if a number is a multiple of 7 or not."""

# x = int(input("Enter a number :"))
# if(x % 7 == 0):
#     print(x, "is a multiple of 7")
# else:
#     print(x, "is not a multiple of 7")


"""Chapter Third Started & Name of the Chapter is List's & Tuples's.
List's in Python.
A built-in data type that stores set of velues.
It can store elements of different types (integer, float, strings etc.)
so let's started with list's. """

# marks = [94.4, 87.4, 95.7, 66.6, 45.2]
# student = ["dhruv", 95.6, 19, "Delhi"]
# student[0] = "jerry"
# len(student)


# marks = [ 94.4, 87.4, 95.7, 66.6, 45.2,]
# name = "Dhruv"
# sub = "[english = 95.4, maths = 87.4, science = 95.7, german = 66.6, french = 45.2,]"
# print(sub)
# print(name)
# print(marks)
# print(len(marks))
# print(marks[0])
# print(marks[1])

# student = ["dhruv", 95.6, 19, "Delhi"]
# print(student)


"""Lists Slicing"""

# marks = [85, 94, 76, 63, 48]
# print(marks[-3:-1])

"""list methods"""

# list = [1, 2, 3]
# list.append(100)
# print(list)

# list = [1, 2, 3]
# print(list.sort())
# print(list)

# list = [ "bnana", "apple", "cherry", "guvava"]
# print(list.sort(reverse=True))
# print(list)

# list = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
# list.reverse()
# print(list)

# list = [2, 1, 3, 4]
# list.insert(1,5)
# print(list)

# list = [2, 1, 3, 1]
# list.remove(1)
# print(list)

# list = [2, 1, 3, 1]
# list.pop(2)
# print(list)

"""Tuples In Python
A built-in data type that stores set of velues.
It can store elements of different types (integer, float, strings etc.)
so let's started with tuple's. """

# tup = (2, 1, 5, 4, 7)
# print(type(tup))
# print(tup[1])

""" That we  want to crete a single value in their tuple in coe with , comma(,)."""

"""Tuple Methods"""

# tup = (1, 2, 3, 4)
# print(tup.index(2))

# tup = (1, 2, 3, 4, 2, 2)
# print(tup.count(2))

"""Let's Practice Q&A of chapter third of List's & Tuples's. 
Q1, Write a program to ask the user to enter name of 3 favorite movies & store them is a list."""

# movies = []
# mov1 = input("enter first movie : ")
# movies.append(mov1)

# mov2 = input("enter second movie : ")   
# movies.append(mov2)

# mov3 = input("enter third movie : ")
# movies.append(mov3)

# print(movies)

# movies = []
# movies.append(input("enter first movie : "))    
# movies.append(input("enter second movie : "))
# movies.append(input("enter third movie : "))

# print(movies)

"""Q2, Write a programe to check if a list contains a palindrome of elements.
(Hint: use copy () method).
[1,2,3,2,1]    [1,"abc", "abc", 1]"""

# list1 = [1, 2, 3]
# list2= [1, 2, 3]

# copy_list1 = list1.copy()
# copy_list1.reverse()

# if(copy_list1 == list1):
#      print("palindrome")
# else:
#      print("NOT palindrome")  


"""Q3, Write a program to count the number of students with th "A" grade in the following tuple.
["C", "D", "A", "B", "B", "A"]"""

# grade = ("C", "B", "A", "A", "A", "B", "B", "A")
# print(grade.count("A"))

"""Q4, Store the above values in a list & sort them from "A" to "D"."""

# grade = ("C", "D", "A", "B", "B", "A")
# print(sorted(grade))
# print(grade)

"""Chapter Fourth Started. Dictonaries & Sets.
Dicitonaries in Python
Dicitonaries are used to store data values in key:value pairs.
They are unordered, mutablen (cgangable) & don't allow duplicate keys."""

# dict = {
#     "name" : "Dhruv Sharma",
#     "age" : 19,
#     "country" : "India",
#     "is_adult" : True,
#     "cgpa" : 12.33,
#     "subjects" : ["python", "java", "julia"],
#     "friends" : ["Dhruv", "Devidson", "Dhruv Sharma"],
#     "mark" : [99, 98, 52,74, 95]
# }


"""First Case"""
# info = {
#     "name" : "Devidson",
#     "age" : 19,
#     "country" : "India",
#     "is_adult" : True,
#     "marks" : [99],
#     "learing" : "python",
# }

# print(type(info))

"""Second Case."""
# info = {
#     "name" : "jerrysmith",
#     "age" : 19,
#     "country" : "India",
#     "is_adult" : True,
#     "marks" : [99],
#     "learing" : ["python", "java", "julia"],
    
# }

# print(type(info))

"""Dicitonary Exampel."""
# info = {
#     "name" : "jerrysmith",
#     "subjects" : ["python", "java", "julia"],
#     "topics" : ("dict","set" ),
#     "age" : 19,
#     "is_adult" : True,
#     14.99 : 95.4
# }

# print(info["name"])
# print(info["topics"])
# print(info["subjects"])
# print(info["age"])

"""We can reassin the value to createded a new key pair."""

# info = {
#     "name" : "jerrysmith",
#     "subjects" : ["python", "java", "julia"],
#     "topics" : ("dict","set" ),
#     "age" : 19,
#     "is_adult" : True,
#     14.99 : 95.4
# }

# info["name"] = "dhruv"
# info["surename"] = "sharma"
# print(info)

"""We want to chang key value in the code."""

# null_dict = {}
# null_dict["name"] = "happy"
# print(null_dict)

"""Dictionary with nested dictonary.
First Case"""
# Studeent = {
#     "name" : "dhruv",
#     "score" : {
#         "phy" : 96,
#         "chem" : 92,
#         "maths" : 90    
#     }
# }

# print(Studeent["score"]["phy"])

"""Second Case"""

# Student = {
#     "name" : "Dhruv",
#     "subjects" : {
#         "phy" : 80,
#         "chem" : 92,
#         "maths" : 52
#     }
# }

# print(Student["subjects"]["chem"])

""" Dictionary Methods
(i) myDict.keys() #returns all keys in dict."""

# Student = {
#     "name" : "Dhruv Sharma",
#     "subjects" : {
#         "chem" : 96,
#         "math" : 85,
#         "phy" : 92
#     }
# }

# print(Student.keys())
# print(len(list(Student.keys())))

"""(ii) myDict.value () #returns all values."""

# Student = {
#     "name" : "Dhruv Sharma",
#     "subjects" : {
#         "chem" : 90,
#         "math" :80,
#         "phy" : 91
#     }
# }

# print(list(Student.values()))

"""(iii) myDict.items() #returns all (key,value) pairs in tuples."""

# Student = {
#     "name" : "Dhruv Sharma",
#     "subjects" : {
#         "chem" : 90,
#         "math" :80,
#         "phy" : 91
#     }
# }

# paris=list(Student.items())
# print(paris[1])

"""(iv) myDict.get("key") #returns the key according to value."""

# Student = {
#     "name" : "Dhruv Sharma",
#     "subjects" : {
#         "chem" : 90,
#         "math" :80,
#         "phy" : 91
#     }
# }

# print(Student["name"])
# print(Student.get("name"))

"""(v) myDict.update(newDict) #inserts the specified items to the dictionary."""

# Student = {
#     "name" : "Dhruv Sharma",
#     "subjects" : {
#         "chem" : 90,
#         "math" :80,
#         "phy" : 91
#     }
# }

# new_dict = {"city" : "delhi ", "age" : 19}
# Student.update(new_dict)

# print(Student)

"""Set in Python.
Set in the collection of the unorderd items.
Each element in the set must be unique & immutable.

nums = {1, 2, 3, 4, 5}
set2 = {1, 2, 2, 2}"""

#reppated elements stored only onec so it resolved to {1, 2}
 
# null_set = set() #empty set syntax
# collection = {1, 2, 3, 4, "hello", "world"}

# print(collection)
# print(type(collection))

# collection = set() #empty dictionary

# print(type(collection))

"""Set Methods
(i) set.add(el) #add an element"""

# collection = set()
# collection.add(1)
# collection.add(2)
# collection.add("jerrysmith")
# collection.add((1, 2, 3, 4))

# print(collection)   

"""(ii) set.remove(el) #remove an element"""

# collection = set()
# collection.add(1)
# collection.add(2)
# collection.add("jerrysmith")
# collection.add((1, 2, 3, 4))

# collection.remove(1)
# print(collection)

"""(iii) set.clear() #empties the set"""

# collection = set()
# collection.add(1)
# collection.add(2)
# collection.add("jerrysmith")
# collection.add((1, 2, 3, 4))

# collection.clear()
# print(len(collection))

"""(iv) set.pop() #removes an random value from the set"""

# collection = {"hello", "world", "jerrysmith", "coding", "with", "dhruv", "python"}
# print(collection.pop())
# print(collection.pop())

"""Second Set methods
(i) set.union(set2) #combines both set values & returns new."""

# set1 = {1, 2, 3}
# set2 = {2, 3, 4}

# print(set1.union(set2)) #{1,2,3,4}

# print(set1)
# print(set2)

"""(ii) set.intersection(set2) #combines common values & returns new."""

# set1 = {1, 2, 3}
# set2 = {2, 3, 4}

# print(set1.intersection(set2)) #{2,3}

"""Let's practice Q&A of chapter fourth of Dictionary's & Set's.
Q1, store following word meanings in python dictionary?
table : "a piece of furniture", "list of facts & figures"
cat : "a small animal"."""

# dictionary = {
#     "cat" : "a small animal",
#     "table" : ["a piece of furniture", "list of facts & figures"]
# }

# print(dictionary)

"""Q2, You are given a list of subjects for students. Assume one classroom in required for 1 subject. How many classroom are needed by all students?
"python", "java", "C++", "python", "javascript", "java","python","java", "C++", "c" """

# subjects = {
#     "python","java", "C++", "python", "javascript", "java",
#     "python","java", "C++", "c"

# }

# print(len(subjects))

"""Q3, Write a program to enter marks of 3 sub from the user and store them in a dictionary. Start with an empty dictionary & add one by one. Use subject name as key & marks as value."""

# marks = {}
# x = int(input("enter phy :"))
# marks.update({"phy":x})

# x = int(input("enter chem :"))
# marks.update({"chem":x})

# x = int(input("enter math :"))
# marks.update({"math":x})

# print(marks)

"""Q4, Figure out a way to store 9 & 9.0 as seprat values in the set.
(You can take help of buil-in data types).."""

# values = {
#     ("float", 9.0),
#     ("int", 9)
    
# }

# print(values)

"""Chapter Fifth Started. LOOPS.
LOOPS in Python > Loops are used to repeat instruction.
While Loops > while condition: #some work

Loops has two types:
1. While loops
2. For loops

While loops example in code.
While Condition: #some work"""

# while True :
#     print("hello")
    
""" Theri are countinues are printed and they are not to stoped any time in their code"""

# count = 1
# while count <= 5 :
#     print("hello")
#     count = count + 1
    
# print(count)

# count = 1
# while count <= 5 :
#     print("hello")
#     count += 1 #there are printed countinue
    
    
# i = 1 
# while i <= 100001:
#     print("ghost rider", i)
#     i+=1
    #the are "i" is showing how many times are printed code.
    
#print number from 1 to 5
# i = 1
# while i <= 5:
#     print(i)
#     i += 1  #they are code is five time print and last line are shows loop ended.
    
    
# i = 6 
# while i >= 1:
#     print(i)
#     i -= 1

# print("loop ended")

# i = 7
# while i >= 9:
#     print(i)
#     i -= 1
    
# print("loopended")  #infinite loop are not exicuted. In their condition is false.


"""Let's Practice Q&A of chapter fifth of Loops.
Q1, Print number from 1 to 200."""

# i = 1 
# while i <= 200:
#     print(i)
#     i += 1
# print("loop ended")

"""Q2, Print the number from 200 to 1."""

# i = 200
# while i >= 1:
#     print(i)
#     i -= 1
# print("loop ended")

"""Q3, Print the multiplication table of a number n."""

# n = int(input("enter a number :"))
# i = 1
# while i <= 10:
#     print(n*1)
#     i += 1

"""Q4, Print the elements of the following list using a loop: 
[1,4,9,16,25,36,49,64,81,100]"""

# nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# idx = 0
# while idx < len(nums):
#     print(nums[idx])
#     idx += 1
    
"""Q5, Search for a number x in this tuple using code :
[1,4,9,16,25,36,49,64,81,100]"""

# nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

# x = 36
# i = 0 
# while i < len(nums):
#     if(nums[i] == x):
#         print("FOUND at idx", i)
#     else:
#         print("finding..")    
#     i += 1  
    
    
"""Break & Continue"""

"(i)"

# i = 1 
# while i <= 8:
#     if i == 4:
#         break
#     print(i)
#     i += 1
# print("end of loop")

# num = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 36, 8, 36]

# x = 36
# i = 0
# while i < len(num):
#     if(num[i] == x):
#         print("FOUND at idx", i)    
#     else:
#         print("finding..")
#     i += 1

# print("end of loop")

"(ii)"

# i = 1 
# while i <= 20:
#     if(i % 2 == 0):
#         i += 1
#         continue
#     print(1)
    
#     i += 1
    
# i = 1
# while 1 <= 20:
#     if(i % 2 != 0):
#         i += 1
#         continue
#     print(1)
    
#     i += 1

"""LOOPS IN PYTHON
Loops are used 
for sequential traversal. For traversing list, string, tuple etc.
for loop
for el in list:
    #some work

for Loop with else.
for el in list:
    #some work
else:
    #wrok when loop ends"""
    
    
# nums = [1, 2, 3, 4, 5]

# for val in nums:
#     print(val)
    
# veggies = ["carrot", "potato", "tmato", "onion"]

# for val in veggies:
#     print(val)
    
# tup = (1, 2, 3, 4, 5, 4, 7, 5, 9, 1)

# for num in tup:
#     print(num)
    
# str = "jerrysmith"

# for char in str:
#     print(char)
    
# str = "jerrywilliam"

# for char in str:
#     print(char)
    
# else:
#     print("END")
    
# str = "jerryhappy"

# for char in str:
#     if(char == "C"):
#         print("C found")
#         break
#     print(char)
    
# print("END")


"""Q&A
Q1, Print the element of the following list using a loop:
[1,4,9,16,25,36,49,64,81,100]"""

# nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# idx = 0
# for el in nums:
#     print(el)
    
    
"""Q2, Search for a number x in this tupple using loop:
[1,4,9,16,25,36,49,64,81,100]"""

# nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

# idx = 0 
# for el in nums:
#     if(el == x):
#         print("number found at idx", idx)
#         break 
#     idx += 1

"""Range
Pange functions retunrn a sequence of numbers, starting from O by default, and increments by 1 (by default), and stops before a specified nuber.
range(start?, stop, step?)"""

# for el in range(5):
#     print(el)
    

# for el in range(1, 5):
#     print(el)
    

# for el in range(1, 5, 2):
#     print(el)

"""(i)(a)"""

# seq = range(1000002)
# for i in seq:
#     print(i)
    
"""(b)"""

# for i in range(250000):
#     print(i)

    
# for i in range(10000):
#     print(i)
    
    
# for i in range(2, 20):
#     print(i)


# for i in range(2, 20, 2):
#     print(i)

"""Code example"""

# for i in range(2, 200, 2):
#     print(i)
    
# for i in range(1, 100, 2):
#     print(i)
    
"""Q&A
Q1, Print Number from 1 to 1000."""

# for i in range(1, 1001):
#     print(i)
    
"""Q2, print number from 20050 to 35000."""

# for i in range(20050, 35001):
#     print(i)
    
"""Q3, Print the multiplication table of a number n."""

# n = int(input("enter the number"))

# for i in range(1, 12):
#     print(n * i)

"""Pass Statement
Pass is a null Statement that does nothinng. It is used as a placeholder for future code."""

# for el in range(10):
#     if(el == 5):
#         pass
#     print(el)
    
# for i in range(500):
#     pass
# if i > 100:
#     pass

# print("some useful work")

"""Q1, Write a function to find te sum of first n number. 
(using while)"""

# n =5 
# sum = 0

# for i in range(1, n+1):
#     sum += i
    
# print("total sum is", sum)

# n = 7
# sum = 0
# i = 1

# while i <= n:
#     sum += i
    
# print("total sum is", sum)

"""Q2, Write a function to find the factorial of first n number.(using for)."""

# n = 5
# fact = 1
# i = 1
# while i <= n :
#     fact *= 1
#     i += 1

# print("factorial =", fact)

# n = 3 
# fact = 1
# i = 1
# while i <= 1:
#     fact *=1
#     i += 1

# print("factorial =", fact)

# n = 5
# fact = 1
# i = 1
# while i <= n:
#     fact *= i
#     i += 1

# print("factorial =", fact)

"""Chapter Sixth Started & name of the chapter is Functions & Recursion.
Functions in Python.
Block of statement that perform a specific task.

def func_name(para1, para2.):
    #some work
    return val

func_name(arg1, arg2.) #function call"""

# def sum(a,b):
#     sum = a + b
#     print(sum)
#     return sum

# a = 10
# b = 20

# sum = a + b
# print(sum)

"""Case First"""
# def calc_sum(a,b):
#     sum = a+b
#     print(sum)
#     return sum 

# a = 10
# b = 20

# sum = a+b
# print(sum)

#more lines of code

# a = 150
# b = 200

# sum = a+b
# print(sum)

#more lines of code

# a = 200
# b = 250

# sum = a+b
# print(sum)

"""CASE Second"""
# def calc_sum(a,b):
#     sum = a+b
#     print(sum)
#     return sum 

# calc_sum(10,20)

# more lines of code

# calc_sum(150,200)

#more lines of code

# calc_sum(200,250)

"""CASE Third"""

# def calc_sum(a,b): #parameters
#     return a+b

# sum = calc_sum(105,2002)
# print(sum)

"""Differ CASE First
average of 3 numbers"""

# def calc_avg(a,b,c):
#     sum = a+b+c
#     avg = sum/3
#     print(avg)
#     return avg

# calc_avg(150,250,350)

#NOTE: return Statement is optional.

"""case second"""

# def calc_avg(a,b,c):
#     sum = a+b+c
#     avg = sum/3
#     return avg

# calc_avg(15000,20000,42000)

"""Functions in Python
Build Function              User defind Function
(i) print()                    
(ii) len()                  
(iii) sum()                 
(iv) min()                  
(v) max()                    """

"""Default Parametrs
Assigning a default value to parameter, which is used when no argument is passed."""

# def calc_prod(a=10, b=20):
#     print(a*b)
#     return a*b

# calc_prod()

"""Let's Practice Q&A. Functions & Recursion.
Q1, Write a function to print the element the lenght of a list.(list is the parameter)"""

# cities = ["delhi", "mumbai", "chennai", "kolkata", "banglore"]
# heroes = ["batman", "superman", "wonder woman", "hulk", "thor"]

# def print_len(list):
#     print(len(list))

# print_len(cities)
# print_len(heroes)

"""Q2, Write a function to print the element of a list in a single line.(list is the parameter)"""

cities = ["delhi", "mumbai", "chennai", "kolkata", "banglore"]
heroes = ["batman", "superman", "wonder woman", "hulk", "thor"]

# def print_len(liist):
#     print(len(list))
        
# def print_list(list):
#     for item in list:
#         print(item, end="  ")

# print_list(heroes)        

"""Q3, Write a function to find the factorial of n.(n is the parameter)"""

# n=5
# def cal_fact(n):
#     fact = 1
#     for i in range(1, n+1):
#         fact *= i
#     print("factorial =", fact)
    
# cal_fact(n)

"""Q4, Write a function to conver US to INR."""

# def converter(usd_val):
#     inr_val = usd_val * 83
#     print(usd_val, "USD=", inr_val, "INR")
    
# converter(5000)

"""Recursion.
When a function calls itself repeatedly."""

#print n to 1 backwards.

# def show(n):
#     if(n == 0):
#         return
#     print(n)
#     show(n-1)
#     print("END")

# show(3)

# def show(n):
#     if(n == 0):
#         return
#     show(n-1)
#     print(n)
    
# show(6)

"""Example of Recursion part 2."""
#return n!

# def fact(n):
#     if(n == 0 or n == 1):
#         return 1
#     else:
#         return n * fact(n-1)
    
# def fact(n):
#     if(n == 1 or n == 0):
#          return 1
#     return fact(n-1) * n

# print(fact(5))

"""Let's Practice Q&A. Functions & Recursion.
Q1, Write a recursive function to calcilate the sum of first n natural numbers."""

# def calc_sum(n):
#     if(n == 0):
#         return 0
#     return calc_sum(n-1) + n

# sum = calc_sum(5)
# print(sum)

"""Q2, Write a recrursive function to print all elements in a list.
HINT: use list & index as parameters."""

# def print_list(list, idx):
#     if(idx == len(list)):
#         return
#     print(list[idx])
#     print_list(list, idx+1)

# frutes = ["apple", "banana", "mango", "orange", "pineapple"]

"""Chapter Eight Stearted & name of the chapter OOPS in python part ONE
(Object Oriented Programming System).
OOP in Python>
To map with real world scenarios, we started using objects in code.
This is called object-oriented programming."""

"""Ex Code"""

# a = 15
# b = 10

# sum = a+b
# print(sum)

# diff = a-b
# print(diff)

"""Class & Objects
Class is a blueprint for creating objects.
#creating class
class student:
    name = "Dhruv Sharma"
    
#creating object (instance)
s1 = student()
print(s1.name) """

"""Two example
(i)"""
# class Student:                                                     
#     name = "dhruv"   
    
# s1 = Student()
# print(s1.name)

# s2 = Student()
# print(s2.name)

"""(ii)"""

# class Car:
#     color = "blue"
#     brand = "Ferrari"
    
# car = Car()
# print(Car.color)
# print(Car.brand)

""" __init__ function
Constructor
All classes have a function called __init__(), Which is always executed when the class is being initiated."""

# creating class
# class Student:
#     def __init__(self, fullname):
#         self.name = fullname

# #creating Object
# s1 = Student("Dhruv Sharma")
# print(s1.name)

"""*The self parametor is a reference to the current instance of the class, and is used to access variables that belongs ro the class.
ex code>>(i)"""

# class Student:
#     name = "Kamal Kant Sharma"
#     def __init__(self):
#         print("adding new student in Database..")
        
# s1 = Student()
# print(s1)

"""(ii)"""
# class Student:
    
#     def __init__(self, fullname):
#         self.name = fullname
#         print("adding new Student in Database..")
        
# s1 = Student("dhruv")
# print(s1.name)

"""(iii)"""
# class Student:
    
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#         print("adding new Student in Database..")
        
# s1 = Student("dhruv", 99)
# print(s1.name, s1.marks)

# s2 = Student("roxi", 90)
# print(s2.name, s2.marks)

"""Class & Instance Attributes"
class.att
obj.att"""

# class Student:
#     college_name = "Jerry College"
#     name = "Morbius"
    
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#         print("adding new Student in Database..")
        
# s1 = Student("Dhruv", 99)
# print(s1.name)

"""Method
Method are functions that belong to obj."""

#creating class                                      
# class Student:                                        
#     def __init__(self, fullname):                   
#         self.name = fullname
        
#     def hello(self):
#         print("hello", self.name)
        
# #creating object

# s1 = Student("dhruv")
# s1.hello()

# class Student:
#     college_name = "Jerry College"
    
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
    
#     def welcome(self):
#         print("welcome student", self.name)
        
#     def get_mark(self):
#         return self.marks
# s1 = Student("Kamal Kant Sharma", 99.4)
# s1.welcome()
# print(s1.get_mark())


"""Let's Practice Q&A Chapter 8.
Object-Oriented Programming System.
Q1, Creat student class that takes name & marks of 3 subjects as arguments in constructor.

Then creat a method to print the average."""

# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
        
#     def get_avg(self):
#         sum = 0
#         for val in self.marks:
#             sum += val
#         print("Hi", self.name, "your avg score is:", sum/3)
        
# s1 = Student("dhruv", [70, 80, 90])
# s1.get_avg()


"""Static Methods>>
Method that don't use the self parameter (work at class level)
class Student:
    @staticmethod
    def college():
        print("jerry college")
        
        
*Decorators allow us to wrap another function in order to extend the bhehaviour of the wrapped function, without permanently modifying it."""
        
# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
        
#     @staticmethod
#     def hello():
#         print("hello")
        
#     def get_avg(self):
#         sum = 0
#         for val in self.marks:
#             sum += val
#         print("Hi", self.name, "your avg score is:", sum/3)
        
# s1 = Student("dhruv", [70, 80, 90])
# s1.get_avg()
# s1.hello()

"""(Important)>>
(i) Abstraction>>
Hiding the implementation of a class and only showing the essential features to the user."""

# class Car:
#     def __init__(self):
#         self.acc = False
#         self.brk = False
#         self.clutch = False
        
#     def start(self):
#         self.clutch = True
#         self.acc = True
#         print("car started")
        
#     def stop(self):
#         self.brk = True
#         print("car stopped")
        
# car1 = Car()
# car1.stop()
# car1.start()

"""(ii) Encapsulation>>
Wrapping of data and functions into a single unit(object)."""

"""Let's Practice Q&A Chapter 8 OOPS.
Q1, Creat Account class with 2 attributes creat method for debit, credit & printing the balance.

Case First"""

# class Account:
#     def __init__(self, balance, acc_no):
#         self.balance = balance
#         self.acc_no = acc_no
        
#     def ddebit(self, amount):
#         self.balance -= amount
#         print("your current balance is:", self.balance)
        
#     def credit(self, amount):
#         self.credit = amount
#         self.balance += amount
#         print("your current balance is:", self.balance)
        
#     def get_balance(self):
#         return self.balance
    
#     def welcome(self):
#         print("welcome", self.name)
        
#     def __str__(self):
#         return "your current balance is: " + str(self.balance)
    

# acc1 = Account(100050, 500025)
# acc1.ddebit(6000)

"""Case Second"""

# class Account:
#     def __init__(self, bal, acc):
#         self.balance = bal
#         self.account_no = acc
        
#     def debit(self, amount):
#         self.balance -= amount
#         print("Rs.", amount, "was debited")
#         print("total balence = ", self.get_balance())
        
#     def credit(self, amount):
#         self.balance += amount
#         print("Rs.", amount, "was credited")
        
#     def get_balance(self):
#         return self.balance
    

# acc1 = Account(100050, 500025)
# acc1.debit(6000)
# acc1.credit(1200)
# acc1.credit(3000)
# acc1.debit(15000)

# print("current balance = ", acc1.get_balance())


"""Chapter 8 OOPS.
Part 2. Let's Started with OOPs. Part 2>>
Objects Orinted Programming System.


Del Keyword>>
Used to delete object properties or object itself.
Example:>>
del s1.name
del s1"""

# class Student:
#     def __init__(self, name):
#         self.name = name
        
# s1 = Student("dhruv")
# print(s1.name)
# del s1.name
# print(s1.name)

"""Private (like) attributes & methods>>
Conceptual Implmentation in Python.

Private attributes & method are meant to be used only within the class and are not accesible from outside the class.

First code"""

# class Account:
#     def __init__(self, acc_no, acc_pass):
#         self.acc_no = acc_no
#         self.__acc_pass = acc_pass
        
#     def reset_pass(self):
#         print(self.__acc_pass)
        
# acc1 = Account(119850, "Mr.Dhruv")

# print(acc1.acc_no)
# print(acc1.reset_pass())

"""(ii)Case:"""
    
# class Person:
#     __name = "anonymous"
    
#     def __hello(self):
#         print("hello Mr. Devil we are happy to we meet's you it's my plasure to meet you.")
        
#     def welcome(self):
#         self.__hello()
        

# p1 = Person()
# print(p1.welcome())

"""Inheritance
When one class (child/ derived) derives the properties & metods of another class (parent/base).

class Car:
    ....
    
class ToyotaCar(Car):
    ...."""
    
# class Car:
#     @staticmethod
#     def start():
#         print("car stopped..")
        
#         @staticmethod
#         def stop():
#             print("car started..")
            
# class ToyotaCar(Car):
#     def __init__(self, name):
#         self.name = name
        
# Car1 = ToyotaCar("Fortuner")
# Car2 = ToyotaCar("Prius")

# print(Car1.start())

""" Inheritance
Type
. Single Inheritance
. Multi-level Inheritance
. Multiple Inheritance"""

# class Car:
    
#     @staticmethod
#     def start():
#         print("car started..")
        
#         @staticmethod
#         def stop():
#             print("car started..")
            
# class ToyotaCar(Car):
#     def __init__(self, brand):
#         self.brand = brand
        
# class Fortuner(ToyotaCar):
#     def __init__(self, type):
#         self.name = type
        
# Car1 = Fortuner("sedan")
# Car1.start()

# class A:
#     varA = "welcome to class A"

# class B:
#     varB = "welcome to class B"

# class C(A, B):
#     varC = "welcome to class C"

# c1 = C()

# print(c1.varC)
# print(c1.varB)
# print(c1.varA)

""" Super method
super() method is used to access method of the parent class."""

# class Car:
#     def __init__(self, type):
#         self.type = type
        
#     @staticmethod
#     def start():
#         print("car started..")
        
#         @staticmethod
#         def stop():
#             print("car Stopped..")
            
# class ToyotaCar(Car):
#     def __init__(self, name, type):
#         super().__init__(type)
#         self.name = name
#         super().start()

# car1 = ToyotaCar("Vertus", "Petrol")

# print(car1.type)

"""class method
A class method is bounde to the class & recives the class as an implicit first argument.
NOTE- static method can't access or modify state & generally for utility.

  class Studenr:
    @classmethod #decorator
    def college(cls):
        pass"""
        
# class Person:
#     name = "Anonyomus"
    
#     def changeName(self, name):
#         Person.name = name
        
#     #self.__class__.person
    
# p1 = Person()
# p1.changeName("dhruv")
# print(p1.name)
# print(Person.name)

"""Second Case:>>"""

# class Person:
#     name = "Anonymous"
    
#     @classmethod
#     def changeName(cls, name):
#         cls.name = name
        
# p1 = Person()
# p1.changeName("dhruv sharma")
# print(p1.name)
# print(Person.name)

"""Property decorator
We use @property decorator on any method in the class to use the method as a property.
(i) @getter
(ii) @setter"""

# class Student:
#     def __init__(self, phy, chem, math):
#         self.chem = chem
#         self.phy = phy
#         self.math = math
        
#         #def clacPercentage(self):
#             #self.percentage = str([self.phy + self.chem + self.math] / 3) + "%"
            
#     @property
#     def percentage(self):
#         return str((self.phy + self.chem + self.math)/3) + "%"


# stu1 = Student(96, 89, 90)
# print(stu1.percentage)

# stu1.phy = 90
# print(stu1.percentage)

# stu1.chem = 96
# print(stu1.percentage)

""" Polymorphism : Operator Overloading
When the same operator is allowed to have differnt meaning according to the contxt.

Operators & Dunder functions
Operator  |  Meaning
a+b #addition          a.__add__(b)
a-b #subtraction       a.__sub__(b)
a*b #multiplication    a.__mul____(b)
a/b #division          a.__truediv____(b)
a%b #addition          a.__mod____(b)"""

# class Complex:
#     def __init__(self, real, img):
#         self.real = real
#         self.img = img
    
#     def showNumber(self):
#         print(self.real, "i +", self.img, "j")
        
#     def __add__(self, num2):
#         newReal = self.real + num2.real
#         newImg = self.img + num2.img
#         return Complex(newReal, newImg)
    
# num1 = Complex(5, 6)
# num1.showNumber()

# num2 = Complex(7, 8)
# num2.showNumber()

# num3 = num1 + num2
# num3.showNumber()

# class Complex:
#     def __init__(self, real, img):
#         self.real = real
#         self.img = img
    
#     def showNumber(self):
#         print(self.real, "i +", self.img, "j")
        
#     def __add__(self, num2):
#         newReal = self.real + num2.real
#         newImg = self.img + num2.img
#         return Complex(newReal, newImg)
    
#     def __sub__(self, num2):
#         newReal = self.real - num2.real
#         newImg = self.img - num2.img
#         return Complex(newReal, newImg)
    
#     def __mul__(self, num2):
#         newReal = self.real * num2.real
#         newImg = self.img * num2.img
#         return Complex(newReal, newImg)
    
# num1 = Complex(5, 6)
# num1.showNumber()

# num2 = Complex(7, 8)
# num2.showNumber()

# num3 = num1 + num2
# num3.showNumber()

# num3 = num1 - num2
# num3.showNumber()

# num3 = num1 * num2
# num3.showNumber()


# class Complex:
#     def __init__(self, real, img):
#         self.real = real
#         self.img = img

#     def showNumber(self):
#         print(self.real, "i +", self.img, "j")
        
#     def __add__(self, num2):
#         newReal = self.real + num2.real
#         newImg = self.img + num2.img
#         return Complex(newReal, newImg)
    
#     def __sub__(self, num2):
#         newReal = self.real - num2.real
#         newImg = self.img - num2.img
#         return Complex(newReal, newImg)
    
# num1 = Complex(5, 6)
# num1.showNumber()

# num2 = Complex(7, 8)
# num2.showNumber()

# num3 = num1 - num2
# num3.showNumber()

# class Complex:
#     def __init__(self, real, img):
#         self.real = real
#         self.img = img
        
#     def showNumber(self):
#         print(self.real, "i +", self.img, "j")
        
#     def __add__(self, num2):
#         newReal = self.real + num2.real
#         newImg = self.img + num2.img
#         return Complex(newReal, newImg)
    
#     def __mul__(self, num2):
#         newReal = self.real * num2.real
#         newImg = self.img * num2.img
#         return Complex(newReal, newImg)
    
# num1 = Complex(5, 6)
# num1.showNumber()

# num2 = Complex(7, 8)
# num2.showNumber()

# num3 = num1 * num2
# num3.showNumber()


"""Let's Practice Q&A Chapter 8 OOPs.

Q1, Define a circle class to create a circle with radius (r) using the constructor.
Which calculates the area() of the circle.
Define a Parameter() method of the class which allows you to calculates the perimeter of the circle."""

# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
        
#     def area(self):
#         return (25/5) * self.radius ** 2
    
#     def perimeter(self):
#         return 2 * (25/5) * self.radius
    
# c1 = Circle(21)

# print(c1.area())
# print(c1.perimeter())


"""Q2, Define a Employee class with attributes role, Department & salary. This class also a showDetails() method.
Create an Engineer class that inherits properties from Employee & has additional attributes: name & age."""

# class Employee:
#     def __init__(self, role, dept, salary):
#         self.role = role
#         self.dept = dept
#         self.salary = salary
        
#     def showDetails(self):
#         print("role =", self.role)
#         print("dept =", self.dept)
#         print("salary =", self.salary)
        
# class Engineer(Employee):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         super().__init__("Engineer", "Software", "120k")
        
# #e1 = Employee("accountent", "Finance", "120k")
# #e1.showDetails()

# engg = Engineer("Dhruv Sharma", 20)
# engg.showDetails()

"""Q3, Create a class Order which store item & its price.
Use Dunder function__gt__() to convey that:
      order1 > order2 if price of order1 > price of order2."""
      
# class Order:
#     def __init__(self, item, price):
#         self.item = item
#         self.price = price
        
#     def __gt__(self, odr2):
#         if self.price > odr2.price:
#             return True
        
# odr1 = Order("milkcake", 1500)
# odr2 = Order("kajukatli", 1000)

# print(odr1 > odr2)