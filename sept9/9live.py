# Nine Lives Game Lab

import random

heart_symbol = u'\u2764'
lives = list(heart_symbol * 9)

words = ["pizza", "fairy", "teeth", "shirt", "otter", "plane"]

secret_word = list(random.choice(words)) # selects random word from list and assigns to secret_word variable

final_word = "".join(secret_word.copy())

clue = list('?????') # question marks stored as list

print("Let's play a game! I'm thinking of a five-letter word.\n")
print(f"Lives = {lives}\n")

while True:
    if (len(lives) > 0) and ("?" in clue): # checks that you still have lives and there are ?s in clue list
        guess = input("Guess a letter: ") # asks for user input for a letter
        print("")
        # for letter in secret_word:
        if guess in secret_word:
            index = 0
            while index < len(secret_word):
                if guess == secret_word[index]:
                    clue[index] = guess
                    index +=1
                else:
                    index += 1    
            print("You guessed correctly!")
            print(clue)
            print(f"Lives = {lives}\n")
        else: # if user does not enter letter in secret word, lose a life
            print("Wrong guess!")
            del lives[-1]
            print(clue)
            if len(lives) >= 1:
                print(f"Lives = {lives}\n")
            else:
                print("Out of Lives\n")
    elif "?" not in clue:
        print(f"You win! The word is {final_word}\n")
        break
    else:
        print("Game over. You lose!\n")
        break
