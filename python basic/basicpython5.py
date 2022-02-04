# basic python progaram
# Based on Dictionar and set
# 1.create dictinar with hindi word and translate in english wrod
mydict={
    "pankha":"fan",
    "stree":"iron",
    "chuha":"mouse",
}
print("your option is",mydict.keys())
choose=input("please choose the option which you want to translate:")
translation=("the translation of this word is",mydict[choose])
print(translation)

# 2.collect 8 eight no from user and storedas unique once
num1=int(input("Enter the no1:"))
num2=int(input("Enter the no2:"))
num3=int(input("Enter the no3:"))
num4=int(input("Enter the no4:"))
num5=int(input("Enter the no5:"))
num6=int(input("Enter the no6:"))
num7=int(input("Enter the no7:"))
num8=int(input("Enter the no8:"))
num=[num1,num2,num3,num4,num5,num6,num7,num8]
print(num)

# 3.create a empty dictionary  aloow 4 freind to enter theire favourite language
favlang={}
a=input("shubham please enter your favrourite language:")
b=input(" naeem enter your favrourite language:")
c=input("shahnawaz please enter your favrourite language:")
d=input("vakil please enter your favrourite language:")
favlang["shubham"]=a
favlang["naeem"]=b
favlang["shahnawaz"]=c
favlang["vakil"]=d
print(favlang)









