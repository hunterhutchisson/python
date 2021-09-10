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


HoustonCities = ["Katy", "Memorial City", "Sugar Land",
                 "The Heights", "River Oaks", "Pasadena"]
ClearLakeCities = ["League City", "Kemah", "Seabrook", "Webster", "El Lago"]

Houston = HoustonCities + ClearLakeCities

# print(len(Houston))

Houston.extend(["Pearland", "The Woodlands", "Deerpark"])

# index = 0
# while index < len(Houston):
#     print(Houston[index])
#     index += 1

# print(len(Houston))

htx1 = Houston[:4]
htx2 = Houston[2:6]
htx3 = Houston[-2:]

print(htx1)
print(htx2)
print(htx3)

Houston.insert(4, "Denver")

print(Houston)

Houston.pop()

print(Houston)

print(Houston.index("Seabrook"))

Houston.sort()

print(Houston)

USCities = Houston.copy()

print(USCities)

Houston.clear()

print(Houston)




# todos = ["pet the cat", "go to work", "shop for groceries", 
# "go home", "feed the cat"]

# prompt = input("Would you like to add anything? If so type it here: ")

# while len(prompt) > 0:
#     todos.append(prompt)
#     print(todos)
#     prompt = input("Would you like to add anything? If so type it here: ")

# print(todos)











