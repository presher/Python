print("Welcome to my computer quiz")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Lets Play :)")
score = 0

answer = input("What does cpu stand for? ")

if answer.lower() == "central processing unit":
    print("That is Correct my Lord! " + answer)
    score += 1
else:
    print("Sorry, my Lord that is incorrect!!")

answer = input("Who is Jesus Christ? ")

if answer.lower() == "savior":
    print("That is Correct my Lord! " + answer)
    score += 1
else:
    print("Sorry, my Lord that is incorrect!!")

answer = input("what does ram stand for? ")

if answer.lower() == "random access memory":
    print("That is Correct my Lord! " + answer)
    score += 1
else:
    print("Sorry, my Lord that is incorrect!!")

answer = input("What is the largest natural formation on Earth? ").lower()

if answer == "grand canyon":
    print("That is Correct my Lord! ", answer)
    score += 1
else:
    print("Sorry, my Lord that is incorrect!!")

print("You got", str(score), "questions correct. For a", str((score/4) * 100), "% score")

