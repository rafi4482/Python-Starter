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

# problem 11
rhyme = "Twinkle, twinkle, little star. How I wonder what you are!"
rhyme = rhyme.lower()
char_count = {}

for char in rhyme:
    if char.isalpha():
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1

print(max(char_count,key=char_count.get))

# problem 12
list1 = [3, 5, 7, 4, 8, 8]
list2 = [4, 9, 8, 7, 1, 1, 13]

dict1 = {}
dict2 = {}
common_items = []

for num in list1:
    if num in dict1:
        dict1[num] += 1
    else:
        dict1[num] = 1

for num in list2:
    if num in dict2:
        dict2[num] += 1
    else:
        dict2[num] = 1

for key in dict1:
    if key in dict2:
        common_items.append(key)

print(common_items)
print(sum(common_items))

# problem 13
dict1 = {'age': 13, 'id': 12, 'address': 'Banani', 'course': 'Python'}
dict2 = {'address': 'Rupnagar', 'id': 25, 'course': 'MERN'}

common_keys = dict1.keys() & dict2.keys()
print(common_keys)

# problem 14
list_1 = [4, 9, 8, 7, 5, 2, 13]
list_1.sort(reverse=True)
print(max(list_1)-min(list_1))

# problem 15

student_1 = [40, 35, 70, 90, 56]
student_2 = [57, 35, 80, 98, 46]

def check_res(marks):
    for mark in range(len(marks)):
        if marks[mark] < 40:
            print("Failed")
            return
        
    average = sum(marks) / len(marks)
    print("Average Marks:", average)    