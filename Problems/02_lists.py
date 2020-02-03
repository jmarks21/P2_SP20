# LISTS (25pts)
# Show work on all problems.  Manually finding the answer doesn't count

# PROBLEM 1 (Using List Comprehensions - 8pts)

print("PROBLEM 1")

# Use list comprehensions to do the following:
# a) Make a list of numbers from 1 to 100

print("\n1a")

my_list = []

for i in range(1, 101):
    my_list.append(i)

print(my_list)

# b) Make a list of even numbers from 20 to 40

print("\n1b")

my_list = []

for i in range(10, 21):
    my_list.append(2 * i)

print(my_list)

# c) Make a list of squares from 1 to 100 (1 ** 2 to 100 ** 2)

print("\n1c")
my_list = []

for x in range(1, 101):
    my_list.append(x ** 2)

print(my_list)

my_list = [x ** 2 for x in range(101)]

# d) Make a list of all positive numbers in my_list below.

print("\n1d")
my_list = [-77, -78, 82, 81, -40, 2, 62, 65, 74, 48, -37, -52, 90, -84, -79, -45, 47, 60, 35, -18]


# PROBLEM 2 (Import the number list - 3pts)
# The Problems directory contains a file called "number_list.py"
# import this file which contains num_list
# Print the last 5 numbers in num_list


# PROBLEM 3 (List functions and methods - 8pts)
# Find and print the highest number in num_list (1pt)
# Find and print the lowest number in num_list (1pt)
# Find and print the average of num_list (2pts)
# Remove the lowest number from num_list (2pt)
# Create and print a new list called top_ten which contains only the 10 highest numbers in num_list(2pts)


# PROBLEM 4 (4pts)
# Find the number which appears most often in num_list?


# CHALLENGE PROBLEMS (2pts)
# TOUGH PROBLEMS, BUT FEW POINTS

# Find the number of prime numbers in num_list?
# Hint: One way is to just start removing the ones that aren't

# Find the number of palindromes
# Hint: This may be easier to do with strings




