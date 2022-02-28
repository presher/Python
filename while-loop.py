count = 0
while count <=10:
    print('inside loop', count)
    count = count + 1

number = int(input('Enter a number'))
count = 10
while count >= 0:
    product = number * count
    print(number, "x", count, "=", product)
    count = count - 1
