name = input("What is your name? ")
print("welcome", name, "to adventure of risk")

answer = input("You walked for 5 miles and come to a fork in the road. Do you choose to go left or right? Type left "
               "or right ").lower()

if answer == 'left':
    answer = input("You come to a river. Do you swim or wade across? Type swim or wade ").lower()

    if answer == 'swim':
        answer = input("You are swimming and you see an aligator heading towards you. Do you choose to continue or go "
                       "back? Type continue or back ").lower()
        if answer == 'back':
            print("The aligator caught you and now you are a tasty snack for later")
        elif answer == 'continue':
            print("You made it a shore in the nick of time")
        else:
            print("You have chosen poorly and were bond and taken as a slave")
    elif answer == 'wade':
        print("you stepped on a hidden aligator and were gobbled up")
    else:
        print("You were abducted by mountain trolls and you lose");

elif answer == 'right':
    answer = input("After traveling for days you come to an old delapedated bridge. Do you wish to cross or find "
                   "another path? (cross/continue)").lower()
    if answer == 'Cross':
        answer = input('the begins to break. DO you want to try and make it or return back? (continue/back) ').lower()
        if answer == 'continue':
            print("you fell to your doom")
        else:
            print("You have made it back to land before the bridge fell. You have won. Congratulations!!!")
    else:
        print("You have decided to continue on your way and you have Won. Congratulations!!")

else:
    print('Not a valid option. Game Over')