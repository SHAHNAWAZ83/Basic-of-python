# basic python progaram
# Based on pattern

# 1.print star
#    *
#  * * *
# * * * * * 
#  n=3

n=3
for i in range(n):
    print(" "*(n-i-1),end=" ")
    print("*"*(2*i+1),end=" ")
    print(" "*(n-i-1))
# 2.print star
# *
# **
# ***
n=3
for i in range(3):
    print("*"*(i+1))
   
# 3.printing star
# ****
# ****
# ****
# ****

num=4
for i in range(num):
    print("*"*(num))
    
    
# 4.printing star
# *
# **
# ***
# ****
# ***
# **
# *
num=int(input("enter the no:"))
for i in range(1,num+1):
    print("*"*(i))
for j in range(num-1,0,-1):
    print("*"*(j))

# 5.pattern printing
#    *
#   **
#  ***
# ****
#  ***
#   **
#    *
num=int(input("enter the no:"))
for i in range(1,num+1):
    print(" "*(num-i)+"*"*(i))
for j in range(num-1,0,-1):
    print(" "*(num-j)+"*"*(j))    
    
# 6.pattern printing
#    * 
#   * *
#  * * *
# * * * *
#  * * *
#   * *
#    *
num=int(input("enter the no:"))
for i in range(1,num+1):
    print(" "*(num-i)+"* "*(i))
for j in range(num-1,0,-1):
    print(" "*(num-j)+"* "*(j)) 
    
# 7.printing star using nested for loop:
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *
n=5
for i in range(n-1):
    for j in range(i+1):
        print("*",end=" ")
    print()
for k in range(n):
    for t in range(k,n):
        print("*",end=" ")
    print()

# 8.printint stars pattern using nested for loop
#           *
#         * *
#       * * *
#     * * * *
#   * * * * *
#     * * * *
#       * * *
#         * *
#           *
n=5
for i in range(n-1):
    for j in range(i,n):
        print(" ",end=" ")
    for k in range(i+1):
        print("*",end=" ")
    print()
for l in range(n):
    for y in range(l+1):
        print(" ",end=" ")
    for p in range(l,n):
        print("*",end=" ")
    print()
    
# 9.star pattern printing using nested for loop
#           * *
#         * * * *
#       * * * * * *
#     * * * * * * * *
#   * * * * * * * * * *
#     * * * * * * * *
#       * * * * * *
#         * * * *
#           * *



n=5
for i in range(n-1):
    for j in range(i,n):
        print(" ",end=" ")
    for k in range(i+1):
        print("*",end=" ")
    for o in range(i+1):
        print("*",end=" ")
    print()
for t in range(n):
    for y in range(t+1):
        print(" ",end=" ")
    for r in range(t,n):
        print("*",end=" ")
    for e in range(t,n):
        print("*",end=" ")
    print()   
          
