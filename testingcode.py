print('Welcome to Wordle!!\nDo you have what it takes to guess todays Wordle?')

correct = 'kirby'

userinput = input("Take a guess:")

while len(userinput) != 5:
    if len(userinput) < 5:
        print('You need to guess a 5 character word.')
        userinput = input ('Take a guess:')

    elif len(userinput) > 5:
        print('You can only guess a 5 character word.')
        userinput = input ('Take a guess:')

if userinput == correct:
    print("Great Job! You got it!")

else:
    print("Guess you're not good enough ;(")