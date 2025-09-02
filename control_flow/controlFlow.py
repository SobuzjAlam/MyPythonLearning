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

#########

# Exercise 09 -> camelCase to snake_case.


def main():
    camelInput = input('camelCase: ')
    snakeCase = convertCase(camelInput)
    print(f'camelCase: {camelInput}\n snake_case: {snakeCase}')


def convertCase(text):
    caseText = []
    for i, char in enumerate(text):
        if char.isupper():
            if i > 0:
                caseText.append('_')
            caseText.append(char.lower())
        else:
            caseText.append(char)
    return ''.join(caseText)


main()

#########

# Exercise 10 -> Coke insert coin.


def main():
    coke_due_price = 50
    print(f'Amount Due: {coke_due_price}')
    coin = 0
    coin_denomination = [25, 10, 5]

    while True:
        insert_coin = int(input('Insert Coin: '))

        if insert_coin in coin_denomination:
            coin = insert_coin + coin
            coke_due_price = coke_due_price - insert_coin

        if coin >= 50:
            print(f'Change Owed: {coin - 50}')
            break

        else:
            print(f'Amount Due: {coke_due_price}')


main()

#########

# Exercise 11 ->  insert emoji.


def main():
    data = input("")
    text = findout(data)
    print(text)


def findout(face):
    face = face.replace(":)", "🙂")
    face = face.replace(":(", "🙁")
    return face


main()

#########

# Exercise 12 ->  Food Time.


def main():
    time = input('What time is it? ')
    given_time = convert(time)
    if 7 <= given_time <= 8:
        print('breakfast time')
    elif 12 <= given_time <= 13:
        print('lunch time')
    elif 18 <= given_time <= 19:
        print('dinner time')


def convert(time):
    hours, minutes = map(int, time.split(':'))
    return hours + minutes / 60

#########

# Exercise 13 ->  Remove vowel from words.


def main():
    user_text = input('Input: ')
    without_vowels = check_vowels(user_text)
    print(f'Output: {without_vowels}')


def check_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    checked_vowels = []
    for chr in text:
        if chr.lower() in vowels:
            checked_vowels.append('')
        else:
            checked_vowels.append(chr)

    return ''.join(checked_vowels)


main()

#########

# Exercise 14 ->  cs50 plate.


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    find_zero = s[2:].find('0')
    if 6 >= len(s) >= 2 and s[0:2].isalpha() and s.isalnum() and find_zero != 0:
        for n in s[2:]:
            if n.isdigit():
                i = s.index(n)
                if s[i:].isdigit():
                    return True
                else:
                    return False
        return True


main()
