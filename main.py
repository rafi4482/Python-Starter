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

print(find_elder(12,13))