# basic python problem
# based on function and recursion
# 1. calculate function of given marks

def percen(marks):
    return(marks[0]+marks[1]+marks[2]+marks[3])/400*100
marks1=[45,74,24,96]
percentage1=percen(marks1)
marks2=[84,84,57,69]
percentage2=percen(marks2)
print(percentage1,percentage2)

# 2.write a program to greet a name using function
def greet(name):
    print("Hello",name)
s=greet("shahnawaz")

# 3.wrtie a program to calculate the sum of two no:
def mysum(num1,num2):
    return(num1+num2)
s=mysum(45,55)
print(s)

#
# 4.write a program to print factorial using function
def factorial(n):
    factorial=1
    for i in range(n):
        factorial=factorial*(i+1)
    return factorial
f=factorial(4)
print(f)

# 5.write a program to print factorial using function
def recursion(n):
    if n==1 or n==0:
        return 1
    return n*recursion(n-1)
r=recursion(4)
print(r)

# 6.write a program to find the greatest of the three no
def maximum(num1,num2,num3):
    if (num1>num2):
        if (num1>num3):
            return num1
        else:
            return num3
    else:
        if num2>num3:
            return num2
        else:
            return num3
       
m=maximum(45,65,88)
print(f"the greatest value of this three no is {m}")
        
# 7.write a program using function to convert celsius into ferenite  
def fereh(cel):
    return (cel*(9/5)+32)
cel=4
f=fereh(cel) 
print(f)  

# 8.write a program using function to convert inches into cm
def cm(inches):
    return(inches*2.54) 
inches=5
c=cm(inches)
print(c)        

# 9 write a recursion functuin to calculate the sum of n natural number
def sum(n):
    if n==1:
        return 1
    else:
        return sum(n-1)+n
m=sum(5)
print(m)

# 10.write a python function to print a multiplication table
def table(n):
    print (f"multiplication table of this {n}")
    for i in range(1,11):
        print(f"{n}x{i}={n*i}")
t=table(6)
print(table)

#11. write a python function to remove word from string from time import time  and strip it at the same time
def remstr(string,word):
    newstr=string.replace(word," ")
    return newstr.strip()
num='    harry shahnawaz you are the best   '
r=remstr(num,"harry")
print(r)        

# 12.  to print fibonacci series 
# fibonacci series:0,1,1,2,3,5,8,13,21
def fibonacci(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return (fibonacci(n-1)+fibonacci(n-2))
n=int(input("enter the no"))
a=fibonacci(n)
print(a)

