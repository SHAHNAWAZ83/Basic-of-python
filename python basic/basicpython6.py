# basic python progaram
# Based on Conditional operator
# 1.find greatest of 4 no by usinf condtional opreter
from tkinter.font import names


num1=int(input("ernter the no:"))
num2=int(input("ernter the no:"))
num3=int(input("ernter the no:"))
num4=int(input("ernter the no:"))
if (num1>num4):
    f1=num1
else:
    f1=num4
if (num2>num3):
    f2=num2
else:
    f2=num3
if (f1>f2):
    print(str(f1)+ "the greatest of four no")
else:
    print(str(f2)+ "the greatest of four no")
    
    
# 2.program to find wether a student pass or not
num1=int(input("enter the marks:"))
num2=int(input("enter the marks:"))
num3=int(input("enter the marks:"))
if (num1<33 or num2<33 or num3<33):
    print("you are fail bcoz you marks is below 33")
elif(num1+num2+num3/3)<40:
    print("you are fail bcoz you marks is below 40")
else:
    print("you are pass")

# 3.spam containing following text or not
"make a lot of money","subscribe","now your turn"
text=input("enter the text:")
if ("make a lot of money"in text):
    spam=True
elif("subscribe"in text):
    spam=True
elif("mow your turn"in text):
    spam=True
else:
    spam=False
if (spam):
    print("the given text is talking about harry")
else:
    print("the given text is not  talking about harry")

# 4.program to find whether a given name username is contain less than 10 character or not
username=input("enter the name")
ulen=len(username)
if ulen<10:
    print("the username containe less than 10 character")
else:
    print("the username containe  more than 10 character")
    
# 5.write aprogram to find out whether name is present in the list or not
names=["shahnawaz","Adnan","vakil","harry"]
name= input("enter the name:")
if "shahnawaz" in name:
    print("The name present in the list")
elif "Adnan" in  name:
    print("The name present in the list")
elif"vakil" in name:
    print("The name present in the list")
elif "harry" in name:
    print("The name present in the list")
else:
    print("your name is notpresent in the list")
    
# 6.write a programe to calculate the student from his marks
# 100_90-"a"
# 90_80-"b"
# 80_70-"c"
# 70_60-"d"
# 60_50-"e"
# 50_40-"f"
marks=int(input("enter the marks:"))
if (marks>90):
    grade="a"
elif (marks>80):
    grade="b"
elif (marks>70):
    grade="c"
elif (marks>60):
    grade="d"
elif (marks>50):
    grade="e"
elif (marks>40):
    grade="f"
else:
    grade="fail"
print("your grade is",grade)

# 7.write a program to find whether the given post is talking about shahanwaz or not
user=input("enter the name:")
if "shahnawaz" in user:
    name=True
else:
    name=False
if (name):
    print("the given post is talking about shahnawaz ")
else:
    print("the given post is not talking about shahanwaz")
    

    