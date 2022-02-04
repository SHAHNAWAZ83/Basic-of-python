# basic python progaram
# Based on loops

# 1.write a program to print 1+50 using while loop
from re import L


i=1
while i<=50:
    print(i)
    i=i+1
print("done")
     
# 2.write a programe to print the content of the list usinf while loop
fruits=["mangoes","watermelon","apple","grapes"]
i=0
while i<len(fruits):
    print(fruits[i])
    i=i+1
print("done")

# 3.write a programe to print the multiplication table using for loop
num=int(input("enter the number:"))
for i in range(1,11):
    print(f"{num}X{i}={num*i}")

# 4.write a programe to print the multiplication table using while loop
num=int(input("enter the number:"))
i=1
while (1,11):
    print(f"{num}X{i}={num*i}")
    i=i+1
    if i==11:
        break      

# 6. write a programe to greet all the name which stored in the list l1 and start with s
l1=["shahnawaz","adnan","sakib","nawab"]
for name in l1:
    if name.startswith("s"):
        print("Hello", name)
        
# 7.write a programe to find wheather a given no is prime og not
num=int(input("enter the no:"))
prime=True
for i in range(2,num):
    if (num%2==0):
        prime=False
    break
if (prime):
    print("the no is prime")
else:
    print("the no is not a prime")
    
# 8.write a programe to find the sum of n natural no n usinf while loop
num=int(input("enter the no:"))
sum=0
i=1
while(i<=num):
    sum=sum+i
    i=i+1
# print(f"the sum n natural no is",num)
print("sum of this","n","natural no is:",sum)

# 9.write a programe to calculate the factorial of  a given no using for loop
num=int(input("enter the no:"))
factorial=1
for i in range(1,num+1):
    factorial=factorial*i 
print(f"the factoraial of this {num} is",factorial)

# 10.print star
#    *
#  * * *
# * * * * * 
#  n=3

n=3
for i in range(n):
    print(" "*(n-i-1),end=" ")
    print("*"*(2*i+1),end=" ")
    print(" "*(n-i-1))
# 11.print star
# *
# **
# ***
n=3
for i in range(3):
    print("*"*(i+1))
    
    
    
    

    

    

    
    
