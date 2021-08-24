import random

attemps = 0
attempCount = 6

print("What's your name?")
name = input()

number = random.randint(1, 20)
print(name + ', introduce a number (1 - 20): ')

while attemps < 6:
    print(str(attempCount) + ' attempts reamining')
    print(' ')	
    attNumber = input()
    attNumber = int(attNumber)

    attemps = attemps + 1
    attempCount = attempCount - 1

    if attNumber < number:
        print('Guess a bigger number:')

    if attNumber > number:
        print('Guess a smaller number:')

    if attNumber == number:
        break

if attNumber == number:
    attemps = str(attemps)
    print(name + ', you guessed the number in ' + attemps + ' attempts')

if attNumber != number:
	number = str(number)
	print('The number was ' + number)