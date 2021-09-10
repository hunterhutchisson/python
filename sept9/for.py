import random

print("Let's play a game! I'm thinking of a five-letter word.")

words = ["pizza", "fairy", "teeth", "shirt", "otter", "plane"]

# secret_word = list(random.choice(words))
secret_word = list("teeth")

clue = list('?????')
print(clue)

heart_symbol = u'\u2764'
lives = [heart_symbol] * 9
print(lives)

while True:
    if (len(lives) > 0) and ("?" in clue): # checks that you still have lives and there are ?s in clue list
        guess = input("Guess a letter: ") # asks for user input for a letter
        for letter in secret_word:
            if letter == guess:
                clue[letter] = guess
                print(clue)
