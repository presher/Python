import random
import time

OPERATORS = ["+", "-", "/", "*"]
MIN_OPERAND = 3
MAX_OPERAND = 12
total_number_of_problems = input("How many problems would you like to attempt? Please enter a valid number: ")
TOTAL_PROBLEMS = 0
while True:
    if total_number_of_problems.isdigit():
        TOTAL_PROBLEMS = int(total_number_of_problems)
        break
    else:
        print("Invalid input. Please enter a valid number")


def generate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)

    expr1 = str(left) + " " + operator + " " + str(right)
    answer1 = eval(expr1)
    return expr1, answer1


wrong = 0
wrong_questions = []

input("Press enter to start")
print("++++++++++++++++++++++++++++")

start_time = time.time()

for i in range(TOTAL_PROBLEMS):
    expr, answer = generate_problem()
    while True:
        guess = input("Problem #" + str(i + 1) + ": " + expr + " = ")
        if guess == str(answer):
            break
        wrong += 1
        wrong_questions.append(expr)

end_time = time.time()
total_time = round(end_time - start_time, 2)

print("++++++++++++++++++++++++++++")
print("Nice Work!! You finished in", total_time, "seconds")

if wrong > 0:
    print("You got", wrong, "wrong answers")
    for element in wrong_questions:
        print("Here are you wrong questions")
        print(element)
else:
    print('Congratulations!! You had no wrong answers')
