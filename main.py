from colorama import Fore, Back


print('Welcome to Wordle!')
maxTurns = 6
word = 'KIRBY'
message = "Try and guess today's wordle: "
guesses = []

#checking if any of the letters are in the correct word
for turn in range(0,maxTurns):
    chars=""
    print(f'{message}', end="")
    userguess = input()
    userguess = userguess.upper()
    print(f'\r', end="")
    
    #changing color based on userguess
    for i,guesscharacter in enumerate(userguess):
        charColor = Fore.WHITE
        charBgColor = Back.RESET

        if guesscharacter.upper() in word.upper():
            charBgColor = Back.YELLOW
            if guesscharacter.upper() == word[i].upper():
                charBgColor = Back.GREEN
                #print(f'{Fore.RED} Correct Position {guesscharacter} == {word[i]}')

        if guesscharacter != " ":
            chars += f'{charColor}{charBgColor}{guesscharacter}'
    guesses.append(chars)

    print('\n--------------------')
    for j,guess in enumerate(guesses):
        print(f'{guess}')
    print(f'{Back.RESET}{Fore.RESET}', end="")
    print(f'--------------------{Back.RESET}{Fore.RESET}')
    message = ""
    if userguess.upper() == word.upper():
        break

if userguess.upper() == word.upper():   
    print("You guessed the word! Good Job!")
else:
    print(f"You failed to guess the word! The word was {word}!")