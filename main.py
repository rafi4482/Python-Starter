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
    
# problem 7
def fizzbuzz(num):
    if (num % 5 == 0) and (num % 3 == 0):
        return "FizzBuzz"
    elif (num % 5 == 0):
        return "Buzz"
    elif (num % 3 == 0):
        return "Fizz"
    else:
        return "Not a Fizz-buzz number"
    
# problem 8
def guess_game():
    user_input = int(input("Enter a number from 1 to 9: "))
    correct_num = 6

    if user_input < 1 or user_input > 9:
        print("Enter a number from 1 to 9")
    elif user_input < correct_num:
        print("Your guess is almost there") 
    elif user_input > correct_num:
        print("Your guess is higher") 
    else:
        print("Your Guess Is Correct!")

# problem 9
my_list = [4, 8, 7, 4,3,6,2,1,9]

for i in range(len(my_list)):
    if my_list[i] == 6:
        print("Number 6 is available in the list")
        
# problem 10
data_list = [13, 24, 'Karim', {'name': 'guru'}, 45, 17]
num_list = []

for i in data_list:
    if type(i) == int:
        num_list.append(i)


