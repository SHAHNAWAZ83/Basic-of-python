# basic python progaram
# Based on String topic

# 1.display user entered name followed by good afternoon
name=input("enter the name please:") 
print("Good Afternoo", name)

# 2.fill this letter template and change the date and name with help of string
letter='''Dear <|NAME|>
        you are selected for this MNC company!
        please join this <|DATE|>
        wishing you thw best
        Thankyou'''
name=input("enter the name:")
date=input("enter the date:")
letter=letter.replace("<|NAME|>",name)
letter=letter.replace("<|DATE|>",date)
print(letter)

# 3.detect the double spaces in string
Name='''hiii everyone i am khan shahnawaz  ajaz ahmed ,i am happy to learn coding'''
print(Name.find("  "))

# 4.remove double spaces by string command in problem no 3
Name='''hiii everyone i am khan shahnawaz  ajaz ahmed ,i am happy to learn python  coding'''
Name.find("  ")
Name=Name.replace("  "," ")
print(Name)

# 5.solve this question with escape sequence character:
# letter='''Dear shahnawaz,This python course is nice! Thanks'''
letter='''Dear shahnawaz,\n\tThis python cour\\se is nice! Thank\'s'''
print(letter)
