# 1. Tip Calculator
# bill = input("What was the bill total? ")
# bill_amount = float(bill)
# while True:
#     service_level = input("How was your service? Choose good, fair, or bad: ")
#     if service_level == "good" or service_level == "fair" or service_level == "bad":
#         if service_level == "good":
#             tip_amount = bill_amount * .20
#         elif service_level == "fair":
#             tip_amount = bill_amount * .15
#         elif service_level == "bad":
#             tip_amount = bill_amount * .10
#         break
#     else:
#         print("please input valid service level")
# print("Tip amount: $" + "%.2f" % tip_amount)
# print("Total amount: $" + "%.2f" % (tip_amount + bill_amount))

# 2. Tip Calculator
# bill = input("What was the bill total? ")
# bill_amount = float(bill)
# while True:
#     service_level = input("How was your service? Choose good, fair, or bad: ")
#     if service_level == "good" or service_level == "fair" or service_level == "bad":
#         if service_level == "good":
#             people = input("Split how many ways? ")
#             numpeople = int(people)
#             tip_amount = bill_amount * .20
#         elif service_level == "fair":
#             people = input("Split how many ways? ")
#             numpeople = int(people)
#             tip_amount = bill_amount * .15
#         elif service_level == "bad":
#             people = input("Split how many ways? ")
#             numpeople = int(people)
#             tip_amount = bill_amount * .10
#         break
#     else:
#         print("please input valid service level")
# print("Tip amount: $" + "%.2f" % tip_amount)
# print("Total amount: $" + "%.2f" % (tip_amount + bill_amount))
# if numpeople != 0:
#     print("Amount per person: $" + "%.2f" % ((tip_amount + bill_amount)/numpeople))


#3. How many coins?

# coins = 0
# print("You have 0 coins.")

# while True:
#     question = input("Do you want another coin? ")
#     if question == "yes":
#         coins +=1
#         print(f"You have {coins} coins.")
#     elif question == "no":
#         break
#     else:
#         print("yes or no?")
# print("bye")

#4. Print a box

# width = int(input("Width? "))
# height = int(input("Height? "))
# height_counter = 0
# space = (width-2) * " " 
# print("*" * width)
# while height_counter < (height - 2):
#     print(f"*{space}*")
#     height_counter += 1
# print("*" * width)

#5. Print a triangle

# print("For a triangle with a width equal to your input, pleae input an odd number")
# width = int(input("How wide would you like your triangle? "))
# space = " "
# counter = 1
# space_counter = int((width - counter)/2)
# while counter <= width and space_counter >= 0:
#     print(space * (space_counter) + "*" * counter)
#     counter += 2
#     space_counter -= 1

#6. Multiplication Table

# number = 1
# while number <= 10:
#     print(f"{number} x 1 = {number * 1}")
#     print(f"{number} x 2 = {number * 2}")
#     print(f"{number} x 3 = {number * 3}")
#     print(f"{number} x 4 = {number * 4}")
#     print(f"{number} x 5 = {number * 5}")
#     print(f"{number} x 6 = {number * 6}")
#     print(f"{number} x 7 = {number * 7}")
#     print(f"{number} x 8 = {number * 8}")
#     print(f"{number} x 9 = {number * 9}")
#     print(f"{number} x 10 = {number * 10}")
#     print("...")
#     number += 1 