# THE PERFECT GUESS PROGRAM


import random
randno=random.randint(1,100)
userguess=None
guess=0

while (userguess!=randno):
    userguess=int(input("enter the no:"))
    guess+=1
    if userguess==randno:
        print("you guess right")
    else:
        if userguess<randno:
            print("please enter higher")
        elif userguess>randno:
            print("please enter lower")
print(f"ramdomly  choose this  {randno}")
print(f"the total guess is {guess}")
with open ("h.txt") as f:
    hiscore=f.read()
if str(hiscore)<str(guess):
    with open("h.txt","w") as f:
        f.write(str(guess))
    print(guess)

elif int(guess)>int(hiscore):
    print(f"you guess it right but you lose bcoz  guess is greater than {hiscore}")

else:
    print("Game finished")
        
    