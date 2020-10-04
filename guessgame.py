secret_number = 11
guesscount = 0 #number of guesses
guesslimit = 3
while guesscount < guesslimit:
    guess = int(input('Guessboss: '))
    guesscount += 1
    if guess == secret_number:
        print('You won!')
        break
else:
    print('Failboss!')