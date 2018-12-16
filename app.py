# Making a shape in python #####
print("   /|")
print("  / |")
print(" /  |")
print("/___|")

print("   /|")
print("  / |")
print(" /  |")
print("/___|")

# 3 types of data: strings, storing numbers (decimal or whole), boolean #####
character_name = "Greg"
character_age = "50.5678213"
is_male = False

# Using print function for string and assigned variables #####
print("There once was a man named " + character_name + ", ")
print("he was " + character_age + " years old. ")

character_name = "Victor"
print("He really liked the name " + character_name + ", ")
print("but didn't like being " + character_age + ".")

# Working with strings: new line, quotation escape(whatever character comes after print quotation  #####
print("Giraffe\nAcademy")
print("Giraffe\"Academy")
print("Giraffe\Academy")

# Storing string in variable, Concatenation : adding string onto string ###
# function : block of code that performs specific operation. Use to modify string and get information about our string.
###
phrase = "Giraffe Academy"

print(phrase + " is cool")

# function upper#
print(phrase.lower())
print(phrase.upper())

# Using function combo #
print(phrase.isupper())
print(phrase.upper().isupper())

# How many characters in string #
print(len(phrase))

# Get individual char in string, strings are accessed starting with 0#
print(phrase[5])

# index function : tell us if & where char (numbers and string) starts in the string #
print(phrase.index("affe"))

# replace function uses two values/parameters, 1st old then new #
print(phrase.replace("Giraffe", "Wakanda"))

# Left off 37 min #





