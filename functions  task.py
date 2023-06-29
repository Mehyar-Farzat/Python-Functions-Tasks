
#1.Create a simple function that takes 2 numbers and print their values

def myvalue1(x,y):
    print('first number is:' , x)
    print('second number is:' , y)

myvalue1 (2,4)
first number is: 2
second number is: 4
-----------------------------------
#2.Create a simple function that takes 2 numbers and return their values

def myvalue2(x,y):
    return x,y
    

b = myvalue2 (2,4)
print(b)
(2,4)
----------------------------------
#3.In the above return function , use keywordarguments when calling the function

def myvalue2(x,y):
    return x,y
    

b = myvalue2(x=2,y=4)
print(b)
(2 , 4)
---------------------------------
#4.In the above return function , give x and y default values of 0 and call the function with no arguments

def myvalue2(x=0,y=0):
    return x,y
    

b = myvalue2()
print(b)
(0,0)
--------------------------------
#5.Create a function that can take any number of arguments and print the sum of them

Method 1:
def mysum1(x,y):         
    return x + y
    
b = mysum1(3,9)
print(b)
12

Method 2:
def mysum1(x,y):
    print(x + y)
    
mysum1(3,9)
12
-------------------------------
#6.Create the same sum function using the lambda

mysum1 = lambda x,y : x+y
print(mysum1(3,9))
12
------------------------------
#7.Call the lambda function at the same definition line

mysum1 = lambda x,y: (x+y); print (mysum1(3,9))
12

OR

print((lambda x, y: x + y)(3, 9))
12
-----------------------------
#8.Write the difference between the local variable and global variable

1 - local variables, are declared within functions
and can only be accessed within that function.

2 -  Global variables, are declared outside of any
function and can be accessed from anywhere in the code.

--------------------------------------------------------
Task

'''
create student
add mark
get avg

'''

class student:
    def __init__(self,name):
        print(f'welcome {name}')
        self.mark = []

    def add_mark(self,mark):
        self.mark.append(mark)
        print(self.mark)

    def get_avg(self):
        print(sum(self.mark)/len(self.mark))
        
s1 = student('Ahmed')
s1.add_mark(20)
s1.add_mark(30)
s1.add_mark(40)
s1.add_mark(50)
s1.add_mark(60)
s1.add_mark(70)

s1.get_avg()

s2 = student('Ali')
s2.add_mark(45)
s2.add_mark(20)
s2.add_mark(30)
s2.add_mark(60)
s2.add_mark(10)

s2.get_avg()
---------------------------------------

Task

'''
Bank
    - create accoutn : name , age , gendoe
    - deposite
    - withdraw
    - view balance
    - show all details

'''

class Clint:

    def __init__(self,name,age,gender):
        print(f'welcome {name}')
        
        self.name = name
        self.age = age
        self.gender = gender

    def clint_detail(self):
        print(f'Name : {self.name}')
        print(f'Age : {self.age}')
        print(f'Gender : {self.gender}')
        print(f'Balance : {self.balance}')
    
class Bank(Clint):

    def __init__(self,name,age,gender):
        super().__init__(name,age,gender)
        self.balance = 0

    def deposite(self,amount):
        self.balance += amount
        print(f'your current balance after deposite : {self.balance}')

    def withdraw(self,amount):
        if amount > self.balance:
            print('not enough balance')
            return
        
        self.balance -= amount
        print(f'your current balance after withdraw : {self.balance}')

    def view_balance(self):
        print(f'your current balance : {self.balance}')

c1 = Bank('Ahmed', 30 ,'male')
c1.deposite(500)
c1.deposite(600)
c1.withdraw(300)
c1.withdraw(1000)
c1.deposite(200)
c1.view_balance()
c1.clint_detail()


