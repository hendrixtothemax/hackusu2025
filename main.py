from colorama import Fore, Back


print('Welcome to Wordle!')
maxTurns = 6
word = 'KIRBY'
message = "Try and guess today's wordle: "

#checking if any of the letters are in the correct word
for turn in range(0,maxTurns):
    userguess = input(f'{message}', end="")
    userguess = userguess.upper()
    print(f'\r', end="")
    
    #changing color based on userguess
    for i,guesscharacter in enumerate(userguess):
        charColor = Fore.WHITE
        charBgColor = Back.RESET

        if guesscharacter.upper() in word:
            charBgColor = Back.YELLOW
            if guesscharacter.upper() == word[i]:
                charBgColor = Back.GREEN
                #print(f'{Fore.RED} Correct Position {guesscharacter} == {word[i]}')
            
                if guesscharacter.upper() == word:
                    charBgColor = Back.GREEN
                    #print(f'{Fore.RED} Correct Position {guesscharacter} == {word[i]}')

        print(f'{charColor}{charBgColor}{guesscharacter}', end="")
    print(f'{Back.RESET} {Fore.RESET}', end="")
    message = ""
    
        

        
        