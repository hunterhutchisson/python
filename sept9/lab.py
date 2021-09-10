# planets = ["Earth", "Jupiter", "Neptune", "Mars", "Saturn", "Mercury", "Uranus", "Venus"]
# print(len(planets))
# index = 0
# while index < len(planets):
#     print(planets[index].lower())
#     index += 1

# planets.append("Pluto")
# print(planets)

# planets.pop()
# print(planets)


# HoustonCities = ["Katy", "Memorial City", "Sugar Land",
#                  "The Heights", "River Oaks", "Pasadena"]
# ClearLakeCities = ["League City", "Kemah", "Seabrook", "Webster", "El Lago"]

# Houston = HoustonCities + ClearLakeCities

# print(len(Houston))

# Houston.extend(["Pearland", "The Woodlands", "Deerpark"])

# index = 0
# while index < len(Houston):
#     print(Houston[index])
#     index += 1

# print(len(Houston))

# htx1 = Houston[:4]
# htx2 = Houston[2:6]
# htx3 = Houston[-2:]

# print(htx1)
# print(htx2)
# print(htx3)

# Houston.insert(4, "Denver")

# print(Houston)

# Houston.pop()

# print(Houston)

# print(Houston.index("Seabrook"))

# Houston.sort()

# print(Houston)

# USCities = Houston.copy()

# print(USCities)

# Houston.clear()

# print(Houston)




# todos = ["pet the cat", "go to work", "shop for groceries", 
# "go home", "feed the cat"]

# prompt = input("Would you like to add anything? If so type it here: ")

# while len(prompt) > 0:
#     todos.append(prompt)
#     print(todos)
#     prompt = input("Would you like to add anything? If so type it here: ")

# print(todos)

# string = "DigitalCrafts"
# rev = ""
# index = len(string) -1
# while index >=0:
#     rev += string[index]
#     index -=1
# print(rev)
# rng = range(10)
# print(rng)

# other_rng = range(6, 17, 2)

# planets = ["Earth", "Jupiter", "Neptune", "Mars", "Saturn", "Mercury", "Uranus", "Venus"]
# for planet in planets:
#     print(planet)

# for city in USCities:
#     print(city)

# for num in other_rng:
#         print(num * 5 )

# rng = range(1,11)
# for num1 in rng:
#     for num2 in rng:
#         print(f"{num1} x {num2} = {num1 * num2}")
#     print("...")

# chapters = ["Python", "Javascript", "HTML/CSS", "Node", "React", "Redux"]
# days = ["mon", "tue", "wed", "thur", "fri", "sat", "sun"]

# for chapter in chapters:
#     print(chapter)
#     for day in days:
#         print(day)

# arr = [4, 2, 5, 7, 23, 6, 5]
# sum = 0
# for num in arr:
#     sum += num
# print(sum)

# largest_number = arr[0]
# for num in arr:
#     if num > largest_number:
#         largest_number = num
# print(largest_number)

#Fizz Buzz



#three number sum
a = [12, 3, 1, 2, -6, 5, -8, 6]
a.sort()
solution = []
for i in range(0, (len(a) -1)):
    l = i +1
    r = len(a) - 1
    while l < r:
        ce = a[i]
        left = a[l]
        right = a[r]
        if (ce + left + right == 0):
            current_zero = []
            current_zero.append(ce)
            current_zero.append(left)
            current_zero.append(right)
            solution.append(current_zero)
            l += 1
        elif (ce + left + right > 0):
            r -= 1
        else:
            l += 1
print(solution)




