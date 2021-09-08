
# Strings
# Learning Python Strings
# "I'm a new developer"

# print("Hello World!") #Hello World!
# print("Hello" + " World") #HelloWorld
# print("3" + "5") #35
# print(3 +5) #8
# print(3.14 * 2) #6.28
# print(True + True) #2

# eight = 8

# print(5 / 2)

# first_name = "Hunter"

# last_name = "Hutchisson"

# print(last_name, first_name)
# print(first_name + " " + last_name)

# found_coins = 20
# magic_coins = 10
# stolen_coins = 3

# result = found_coins + magic_coins * 365 - stolen_coins * 52

# print(result) #3514


# #Hello Hunter Hutchisson, how are you doing today?

# sentence = "Hello {1} {0}, how are you doing today?".format(first_name, last_name)
# sentence = "Hello {first} {last} {first}, how are you doing today?".format(first=first_name, last=last_name)
# sentence2 = "Hello {} {}, how are you doing today?".format(first_name, last_name)
# sentence3 = "Hello {} {}, how are you doing today?".format(first_name, last_name)
# print(sentence)

# first_name = "Hunter"
# last_name = "Hutchisson"

# sentence = f"Hello {first_name} {last_name} how are you doing today?"
# print(sentence)

# print(type(9.9))

# print(isinstance("99", int))

# print(abs(-5))

# name = input("What is your name? ")

# print(f'Your name is {name}')

# while True:
#     answer = input("Say when: ")
#     if answer.lower() == "when":
#         break
# print("outside while loop")

number = 0
while number != "stop":
    number = input("input a number: ")
    if int(number) % 2 == 0:
        print(str(number) + " is even")
    else:
        print(str(number) + " is odd")
