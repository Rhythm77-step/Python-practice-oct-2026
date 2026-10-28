"""greeting="Hello"
name="Rhythm"
message=f"{greeting}, {name}. Welcome!"
print(message)
print(dir(str))
print(help(str))
print(help(str.lower))
#mathematical operations
num1=3
print(type(num1))
num2=3.14
print(type(num2))
print(3+2)
print(3-2)
print(3*2)
print(3/2)
print(3**2)
print(3//2)
print(3%2)

print(2%2)
print(3%2)
print(4%2)
print(5%2)
print(3*(2+1))

num=1
num*=10
print(num)
print(abs(-3))
print(round(3.44,1))
num_1=12
num_2=34
print(num_1==num_2)
print(num_1 != num_2)
print(num_1 > num_2)
print(num_1 < num_2)
print(num_1 >= num_2)
print(num_1 <= num_2)

num_1="100"
num_2="200"
num_1=int(num_1)
num_2=int(num_2)

print(num_1+num_2)

courses= ["Maths","Chemistry","Dld","Python"]
print(courses)
print(len(courses))
print(courses[0])
print(courses[2])

print(courses[0:2])
print(courses[:2])
print(courses[2:])
courses_2=["DSA","English"]

print(courses)
courses.sort(reverse=True)
print(courses)
sorted_courses=sorted(courses)
print(sorted_courses)

print(courses)

courses=["maths","art","Python","Java"]
courses.sort()
print(courses)
nums=[23,4,12,78]
nums.sort(reverse=True)
print(nums)
print(min(nums))
print(max(nums))
print(sum(nums))
print(courses.index("Python"))
print("Python" in courses)
for course in courses:
    print(course)
for index,course in enumerate(courses):
    print(index,course)
course_str= '-'.join(courses)
print(course_str)
string="Rhythm-Tripathi-Amarpatan"
new_str=string.split('-')
print(new_str)
list_1=["Maths","python","Java"]
list_2=list_1
list_2="Art"
print(list_1)
print(list_2)

tuple_1=("Rhythm","pravi","Amarpatan")
tuple_2=tuple_1
tuple_2="Art"
print(tuple_1)

courses_1={"Maths","Python","java"}
courses_2={"Hindi","digitallogic","Python","Java"}
print(courses_1.intersection(courses_2))
print(courses_1.difference(courses_2))
print(courses_1.union(courses_2))

empty_list=[]
empty_tuple=()
empty_set=set()
print(empty_set)
print(empty_set)
print(empty_list)
print(empty_tuple)
"""
student={1:"Rhythm", "age":20,"courses":["Python","Java"]}
#print(student)
#print(student[1])
#print(student["courses"])
"""
print(student.get("age"))
print(student.get("courses"))
print(student.get('phone','Not found'))
student["gender"]="male"
student.update({1:"Peter", "age":21})
print(student)

print(len(student))
print(student.keys())
print(student.values())
print(student.items())

for key in student:
    print(key)
for key,value in student.items():
    print(key,value)

language="kotlin"
if language=="python":
    print('Language is Python')
elif language=="java":
    print('Langauge is Java')
elif language=='javascript':
    print('Language is Javascript')
else:
    print('No match')
    
user='Admin'
logged_in= False
if user=='Admin' and logged_in:
    print('Admin Page')

else:
    print('Bad Creds')
logged_in=True
if not logged_in:
    print('Please log in')
else:
    print('Welcome')

user='None'
logged_in=False
if user=='Admin' or logged_in:
    print('Admin page')

else:
    print('Bad Creds')
a=[12-14]
b=[12-14]
print(a==b)
print(a is b)
print(id(a))
print(id(b))
print(id(a)==id(b))

condition='Test'
if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')

nums=[3,4,5,6,7]
for num in nums:
    for letter in 'abc':
        print(num,letter)

for i in range(10):
    print(i)
for i in range(1,11):
    print(i)

x=0
while x<10:
    print(x)
    x+=1

x=0
while x<10:
    if x==5:
        break
        
    print(x)
    x+=1

x=0
while True:
    print(x)
    x+=1
    """
#defining an empty function 
def hello_func():
    print("hello function")

hello_func()    








    





























         

    


































































