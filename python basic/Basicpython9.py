# Basic python problem
# Based on file
# 1. write program to read file and check whether its contain twinle or not
with open("poem.txt") as f :
    content=f.read()
if "Twinkle" in content:
    print("yes Twinkle present in the  file")
else:
    print("no Twinkle is not present in the file")
    
# 2. game play by user 
def game():
    return 45
score=game()
with open("hiscore.txt") as f:
    hiscore=int(f.read())
if hiscore < score:
    with open ("hiscore.txt","w") as f :
        f.write(str(score))
        print(score)

# 3.same as Q2 with empty high score
def game():
    return 65
score=game()
with open ("hiscore.txt") as f:
    hiscore=f.read()
if hiscore=="":
    with open ("hiscore.txt","w") as f :
        f.write(str(score))
        print((score))
        
# 4. write a program to print multipliction table for 2 to 20 and stored to different file
for i in range(2,21):
    with open(f"Table/Multiplicatio  table of this {i}.txt","w") as f:
        for j in range(1,11):
            f.write(f"{i}x{j}={i*j}")
            if j!=10:
                f.write("\n")
            
# 5.write programe to replace a word donkey in file 
with open ("sample.txt") as f :
    content=f.read()
content=content.replace("donkey","#@$%^%")
with open ("sample.txt","w") as f:
    f.write(content)
    
# 6.wrtie a program to censored the a bad word 
# 1st method
with open("sample2.txt") as f:
    content=f.read()
content=content.replace("fool","@#$%^&*")
content=content.replace("dumb","@#$%^&*")
content=content.replace("rubbish","@#$%^&*")
with open("sample2.txt","w")as f:
    f.write(content)

# 2nd method
word=["fool","dumb","rubbish"]
with open("sample2.txt") as f:
    content=f.read()
for word in content :
    content=content.replace("fool","@#$%^&")
    content=content.replace("dumb","@#$%^&")
    content=content.replace("rubbish","@#$%^&")
    with open("sample2.txt","w") as f:
        f.write(content)
        
# 7.write a program to mine a log file and find its contain python or not
with open("log.txt") as f:
    content=f.read()
if "python " in content.lower():
    print("yes python is present in the log file")
else:
    print("no python is not present in the log file")
    
# 8.write a program to mine a log file and find its contain python or not find line no also
conten=True
i=1
with open("log.txt") as f:
    while content:
        content=f.readline()
        if "python" in content.lower():
            print(content)
            i+=1
            print(f"yes python present in the line:{i}")

# 9. make a copy of text file in "this.txt"
with open("text.txt") as f:
    content=f.read()
with open("copy.txt","w") as f:
    f.write(content)   

# 10.check two file content is same or not
file1="text.txt"
file2="copy.txt"       
with open (file1) as f:
    f1=f.read()
with open (file2) as f:
    f2=f.read()
if f1==f2:
    print("yes both are identically same")
else:
    print(" both are not  identically same")

# 11. write a program to wipe uout any file content
with open("text.txt") as f:
    content=f.read()
with open("text.txt","w") as f:
    f.write(" ")

# 12.write a program to remove oldfile name with new file name
import os
oldname="sample.txt"
newname="removebypython.txt"
with open(oldname) as f:
    content=f.read()
with open(newname,"w") as f:
    f.write(content)
os.remove(oldname)


            
