# problem 1 
name = "Hello there"
print(len(name))

# problem 2
name = "Hello there"
print(type(name))

# problem 3
def find_elder(age1,age2):
    if age1 > age2:
        return f"First brother is older ages {age1}"
    else:
        return f"Second brother is older ages {age2}"


# problem 4
numbers=[3, 5, 1, 9, 7, 2, 8 ]
print(numbers.index(7))

# problem 5
numbers=[3, 5, 1, 9, 7, 2, 8 ]
numbers.sort()
print(numbers)

# problem 6
def isLandscape(width,height):
    if width > height:
        return "Landscape"
    else:
        return "Potrait"
    
