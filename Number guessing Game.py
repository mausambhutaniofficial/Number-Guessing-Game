# this is the modified version of Number guessing game and also it takes any random no as winning 
# number. also it takes input frm user till user guesses the right number,also prints the no of
# attempts user has done to guess

#first we'll study about DRY principle of coding
# Don't Repeat Yourself  (dec lines of code)
# in previous program we've written the same 2 lines code in if-else block of the loosing block
# we'll modify that

import random

win_no=random.randint(1,100)
guess=1     # count of attempts user made
game_over=False
print("**Let's check your luck**")
num=int(input("Enter a number between 1 and 100: ")) 

while not game_over:
    if num==win_no and guess==1:  #This if-elif block is "winning block" means when guessing is right
        print("WOW you guessed it right in first attempt!")
        game_over=True
    elif num==win_no:
        print(f"Congrats! You guessed it right in {guess} attempts")
        game_over=True

    else:   #This else block is "loosing block" means when guessing is wrong
        if num < win_no:
            print("Awww! Too low")
        else:
            print("Awww! Too high")
#now we've removed these 2 same lines from each if-else but it will be remained in outer 
# else block i.e, the "loosing block"
        guess+=1
        num=int(input("Guess again: "))
        #this is DRY