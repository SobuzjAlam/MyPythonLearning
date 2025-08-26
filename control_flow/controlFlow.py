# basic control flow

"""
Basic control flow -> 
    Mix of if/else, loops, break, continue, logical operators, nested conditions ...
"""


# Exercise 01 -> Classify age

classify_age_num = 120
result_01 = 'Child' if classify_age_num < 13 else (
    'Teen' if classify_age_num < 19 else 'Adult' if classify_age_num < 60 else 'Senior')
# print(result_01)

#########

# Exercise 02 -> Check if a number is divisible by 5 and 11

divisible_num = 55
result_02 = f'Divisible: {divisible_num}' if (
    divisible_num % 5 == 0 and divisible_num % 11 == 0) else f'Not Divisible: {divisible_num}'
# print(result_02)

#########

# Exercise 03 -> Given 3 sides, check if they form a triangle (triangle inequality)

sides_a = 3
sides_b = 4
sides_c = 5

result_03 = 'Valid triangle' if (sides_a + sides_b > sides_c and sides_b +
                                 sides_c > sides_a and sides_c + sides_a > sides_b) else 'Invalid'
# print(result_03)

#########

# Exercise 04 -> Check if a character is a vowel or consonant


def checking_character(char):
    vowel = ['a', 'e', 'i', 'o', 'u']
    if char.lower() in vowel:
        return 'Vowel Character'
    else:
        return 'Consonant'


result_04 = checking_character('U')
# print(result_04)


#########

# Exercise 05 -> Print numbers from 1 to 20 using a for loop.

for n in range(1, 21):
    print(n)

#########

# Exercise 06 -> Print even numbers from 1 to 50.

for n in range(1, 51):
    if n % 2 != 0:
        print(n)

#########

# Exercise 07 -> Print the multiplication table of a number (e.g., 7).

checking_table_num = 7
for i in range(1, 11):
    print(f'{checking_table_num} x {i} = {checking_table_num * i}')

#########

# Exercise 08 -> Find the sum of first N natural numbers.


def sum_natural_num(n):
    total = 0
    for i in range(1, n+1):
        total += i
    return total


print(sum_natural_num(10))
