number = 7

guess_count = 0
guess_limit = 5
while guess_count < guess_limit:
    entry = int(input('Guess: '))

    if entry == number:
        print('You win!')
        break
    guess_count = guess_count + 1

else:
    print('You loose!')
