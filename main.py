#adding colorama
from colorama import Fore, Back
import random

#setting up correct word for user to guess
print('Welcome to Wordle!')

#declaring the max amount of guesses a user gets
maxTurns = 6

five_letter_words = [
    "apple", "beach", "chair", "dance", "eagle", "fancy", "glove", "haste", "input", "jolly",
    "knife", "liver", "mango", "night", "open", "pearl", "quizy", "rosey", "stare", "touch",
    "under", "vigor", "waste", "xenon", "yearn", "zesty", "brave", "clash", "dealt", "echoes",
    "flame", "gloom", "hatch", "impose", "jumpy", "lapse", "meant", "neckl", "opted", "pines",
    "quest", "relic", "saltz", "tiger", "upset", "vigor", "wound", "xotic", "yawns", "zebra",
    "acorn", "blush", "candy", "dingo", "elite", "fancy", "gear", "hype", "hopes", "inlay", 
    "juice", "klutz", "latch", "myths", "note", "oiled", "packy", "quiz", "rubin", "swoon", 
    "shaky", "toner", "taste", "union", "vood", "whale", "xaxis", "yobbe", "zeroed"
]

# choose a random word from the word list
word_index = random.randrange (0, len(five_letter_words) -1)
word = five_letter_words[word_index]

# magic values
message = "Try and guess today's wordle: "
guesses = []

# running a turn of wordle
for turn in range(0,maxTurns):
    chars=""
    print(f'{message}', end="")
    userguess = input()
    userguess = userguess.upper()
    print(f'\r', end="")

    #make sure user input is valid (only 5 characters)
    while len(userguess) != 5:
        if len(userguess) < 5:
            print('You need to guess a 5 character word.')
            userguess = input ('Take a guess:')

        elif len(userguess) > 5:
            print('You can only guess a 5 character word.')
            userguess = input ('Take a guess:')
    
    #changing color based on userguess
    for i,guesscharacter in enumerate(userguess):
        charColor = Fore.WHITE
        charBgColor = Back.RESET

        # if the character is in the word
        if guesscharacter.upper() in word.upper():
            charBgColor = Back.YELLOW

            # if the character is in the correct spot
            if guesscharacter.upper() == word[i].upper():
                charBgColor = Back.GREEN

        # make sure the character is not a space character
        if guesscharacter != " ":
            chars += f'{charColor}{charBgColor}{guesscharacter}{Back.RESET}{Fore.RESET}'
    guesses.append(chars)

    # print out all the user's guesses
    print('\n--------------------')
    for j,guess in enumerate(guesses):
        print(f'[{j+1}] {guess}')
    print(f'{Back.RESET}{Fore.RESET}', end="")
    print(f'--------------------{Back.RESET}{Fore.RESET}')
    message = ""

    # check if the user has guessed the correct word
    if userguess.upper() == word.upper():
        break

if userguess.upper() == word.upper():   
    print("You guessed the word! Good Job!")
else:
    print(f"You failed to guess the word! The word was {word}!")
print()