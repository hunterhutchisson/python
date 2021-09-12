#1. Multiply Vectors

# vec1 = [2, 4, 5]
# vec2 = [2, 3, 6]
# solution = []
# index = 0
# while index < len(vec1):
#     multiply = vec1[index] * vec2[index]
#     solution.append(multiply)
#     index  += 1
# print(solution)

# or

# for i in range(len(vec1)):
#     solution.append(vec1[i] * vec2[i])
# print(solution)

#2. Matrix Addition

# matrix1 = [[1, 3], [2, 4]]
# matrix2 = [[5, 2], [1, 0]]
# solution = []
# for outer_index in range(len(matrix1)):                                                   #looks at the total length of matrix
#     matrix3 = []
#     for inner_index in range(len(matrix1)):                                               #looks at total length of matrix (since inner and outer have same length doesn't matter)
#         addition = matrix1[outer_index][inner_index] + matrix2[outer_index][inner_index]  #adds parts of the inner matrix from the outer matrix then adds them
#         matrix3.append(addition)                                                          #adds the additions to the matrix3
#     solution.append(matrix3)                                                              #adds the matrix3 to the solution
# print(solution)

#3. Matrix Addition 2
#Use your solution in Matrix Addition, 
#and extend it to work for a pair of matrices of any size, 
#as long as they have the same size.

# matrix1 = [[1, 5, 4], [2, 3, 6], [5, 7, 9], [4, 2, 1]]
# matrix2 = [[5, 2, 9], [1, 0, 3], [4, 5, 8], [8, 7, 3]]
# solution = []
# for outer_index in range(len(matrix1)):                                                   #looks at the total length of matrix
#     matrix3 = []
#     for inner_index in range(len(matrix1[outer_index])):                                  #looks at length of that outer matrix
#         addition = matrix1[outer_index][inner_index] + matrix2[outer_index][inner_index]  #adds the specific index of outer,inner then adds corresponding parts
#         matrix3.append(addition)                                                          #add the addition to matrix 3
#     solution.append(matrix3)                                                              #add matrix3 to solution
# print(solution)

# ???

#4. De-bup

# nums = [1, 2, 3, 4, 4, 5, 2, 3, 10]
# new_nums = []
# for num in nums:                          #looks at each number in numbers
#     if num not in new_nums:               #if the number is not in the new list new nums
#         new_nums.append(num)              #put the number in new nums
# print(new_nums)

#5. Leetspeak

# string = input("Type Something: ").upper()    #we want whatever they enter to be in upper case
# leet_string = ""
# for letter in string:                         #we want to look at each letter (should be char not letter since look at each individual piece)
#     if letter == "A":                         # if the letter is an "A"
#         letter = "4"                          #change the letter to 4 as a string
#     if letter == "E":                         
#         letter = "3" 
#     if letter == "G": 
#         letter = "6" 
#     if letter == "I": 
#         letter = "1" 
#     if letter == "O": 
#         letter = "0" 
#     if letter == "S": 
#         letter = "5" 
#     if letter == "T": 
#         letter = "7" 
#     leet_string += letter                     #we want to add letter(char) changed or original
# print(leet_string)

#6. Long Vowels
# word = "cheese"
# long_word = ""
# for i in range(len(word)):                  # want to cycle through each letter
#     if i < len(word)-1:                     # want to end cycle at second to last letter otherwise following letter out of index
#         letter = word[i]                    # we want the actual letter not just the index
#         following_letter = word[i + 1]      # we want the letter following our letter
#         if letter == following_letter:      # if the letter and the following letter are the same
#             letter = letter * 4             # we want 4 of the letter, then the following letter will give us the 5th
#     else:                                   # when we are on the last index there is no follow_letter so we just want the letter
#         letter = word[i]      
#     long_word += letter                     # we want to add letter regardless of multiply to our long_word
# print(long_word)

#7. Caesar Cipher

# string = "lbh zhfg hayrnea jung lbh unir yrnearq"
# alpha = "abcdefghijklmnopqrstuvwxyz"
# translated = ""                                             #this will be the translated sentence
# offset = 13
# for char in string:                                         #we want to look at every character in the string
#     if char in alpha:                                       # if the character is a letter and not " "
#         if alpha.index(char) < (len(alpha)-1)/2:            #we want index under half the length for addition. if over 12 out of index
#             new_letter = alpha[alpha.index(char) + offset]  #new letter is at index 13 spaces from original
#         else:                                               #we want index over half the length for subtract. 
#             new_letter = alpha[alpha.index(char) - offset]  #new letter is at index 13 spaces from original
#     else:                                                   # we want to leave anything other than letter as is
#         new_letter = char
#     translated += new_letter                                #adds new_letter to translated
# print(translated)