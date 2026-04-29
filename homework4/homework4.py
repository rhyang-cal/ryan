# --- List Operations ---

favorite_foods = ["kimchi stew", "sushi", "steak", "fried rice", "boba"]

print(favorite_foods[1])

print(favorite_foods[-1])

favorite_foods.append("mashed potatoes")

favorite_foods.insert(0, "apple")

del favorite_foods[2]

print(len(favorite_foods))

for i in favorite_foods:
    print(i.upper())

new_food_list = favorite_foods[:1] + favorite_foods[-1:]

if "potato" in favorite_foods:
    print("A potato!")
else:
    print("No potato!")

# --- Slicing and Striding ---

numbers = range(21)

def get_first_15(numbers):
    return numbers[:15]

def get_every_5th(lst):
    return lst[::5]

def reverse_and_stride(lst):
    reversed = lst[::-1]
    return reversed[::3]

step1 = get_first_15(numbers)
step2 = get_every_5th(step1)
step3 = reverse_and_stride(step2)

# --- Nested Lists ---

numbers = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(numbers[2])
print(numbers[2][1])
numbers.append([10,11,12])
def sum_nested(lst):
    total = 0
    for i in lst:
        total += sum(i)
    return total

# --- Create a 5x5 List ---

def new_5x5_list():
    lst = []
    counter = 1
    for i in range(5):
        inner_list = []
        for i in range(5):
            inner_list.append(counter)
            counter += 1
        lst.append(inner_list)
    return lst

five_x_five = new_5x5_list()

def mult_3(lst):
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if lst[i][j] % 3 == 0:
                lst[i][j] = '?'
    return lst

mult3 = mult_3(five_x_five)

def not_q(lst):
    sump = 0
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if lst[i][j] != '?':
                sump += lst[i][j]
    return sump

summed_list = not_q(mult3)

# --- Dictionary Operations ---

ages = {
    "Katie": 30,
    "Mariam": 42,
    "Safia": 25,
    "Mira": 48
}

print(ages["Katie"])
ages["Mariam"] = 100
ages["Milana"] = 52
del ages["Mariam"]

def loop(ages):
    for name, age in ages.items():
        print(f"Name: {name}, Age: {age}")

loop(ages)

print(new_5x5_list())