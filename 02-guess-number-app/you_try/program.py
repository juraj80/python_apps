from random import randint

print('-----------------------------------------')
print('         GUESS THAT NUMBER GAME')
print('-----------------------------------------')
print()



random_guess = randint(0,100)

while True:

    user_guess = int(input('Guess a number between 0 and 100: '))
#    print(random_guess)

    if user_guess == random_guess:
        print("YES. You've got it. The NUMBER was " + str(user_guess))
        break

    elif user_guess < random_guess:
        print('Sorry but ' + str(user_guess) + ' is LOWER than a NUMBER.')

    else:
        print('Sorry but ' + str(user_guess) + ' is HIGHER than a NUMBER.')


