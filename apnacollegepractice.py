"""user_name="Rhythm"
print("Length of user name is:",len(user_name))
dollar_str="I am $ Rhythm $$."
print(dollar_str.count("$"))
#Traffic light system(if-elif-else)

light="black"
if light=="green":
    print("Light is green,you can go")
elif light=="yellow":
    print("light is yellow,please wait")
elif light=="red":
    print("Light is red,stop")
else:
    print("Light is broken")
    

#Student grade calculator
marks=67
if marks>=90:
    grade="A"
elif marks >=80:
     grade="B"
elif marks >=70:
     grade="C"
else:
     grade="D"
print(F"Your marks are {marks},and your grade is {grade}")

#Odd or even check
number=46
if number % 2==0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")

#Greatest of three numbers
n1,n2,n3= 23,45,12
if n1>=n2 and n1>=n3:
    largest=n1

#Multiple of 7 check
num=32
if num % 7 ==0:
    print(f"{num} is divisible by 7")
else:
    print(f"{num} is not divisible by 7")
"""
#List and Tuples
marks=[32.9,76.9,56,43]
"""print("Original list",marks)
marks[0]=99
print("list after upadting marks",marks)
marks.append(97)
print("list after appending new marks:",marks)
marks.sort()
print("list after sorting in ascending order:",marks)
marks.sort(reverse=True)
print("list after sorting data in descending order:",marks)
print(marks)
marks.reverse()
print("list after reversing the order of the elements:",marks)
marks.insert(1,99.9)
print("list after adding marks at a specific position:",marks)"""
print(marks)
marks.pop(1)
print(marks)
#palindrome list checker
list=["a","b","b","a"]
list_copy=list.copy()
list_copy.reverse()
if list_copy==list:
    print(f"list {list} is a palindrome")
else:
    print(f"list {list} is not a palindrome")

#creating list of favourite movies   
movies=[]
movies.append("Harry potter")
movies.append("Spider Man-The End game")
movies.append("Sultan")
movies.append("Taare zameen par")
print("List of favourite movies:",movies)

#tuple basics and Methods
tup=("a","Rhythm",34,"harry",876,"Rhythm")
print("Tuple:",tuple)
print("Count of Rhythm:",tup.count("Rhythm"))
print("Index of 34:",tup.index(34))





































