# basic control flow

"""
Ternary operators -> 
    Conditional expressions, It evaluates a condition and returns one of two values.
    ***[value_if_true if condition else value_if_false]**
"""

# Exercise 01 -> Even or Odd

checking_num = 7
result_01 = 'Even' if checking_num % 2 == 0 else 'Odd'
# print(result_01)

#########################

checking_list = list(range(1, 101))


def checkingOddEvenList(list):
    odd_list = []
    even_list = []
    for i in list:
        if ('Even' if i % 2 == 0 else 'Odd') == 'Odd':
            odd_list.append(i)
        else:
            even_list.append(i)

    return (f'ODD List: {odd_list} \nEVEN List: {even_list}')


result_02 = checkingOddEvenList(checking_list)
# print(result_02)

########
# Exercise 02 -> Positive, Negative, or Zero

checking_classification = -3
result_03 = 'Positive' if checking_classification > 0 else (
    'Zero' if checking_classification == 0 else 'Negative')
# print(result_03)

########
# Exercise 03 -> Max of Two Numbers

checking_num_a, checking_num_b = 120, 20
result_04 = checking_num_a if checking_num_a > checking_num_b else checking_num_b
# print(result_04)

########
# Exercise 04 -> Non negative/absolute value

checking_negative = -15
result_05 = checking_negative if checking_negative >= 0 else abs(
    checking_negative)
# print(result_05)

########
# Exercise 05 -> Non-eligible/eligible

checking_eligible = 20
result_06 = 'Eligible' if checking_eligible >= 18 else 'Non-eligible'
# print(result_06)

########
# Exercise 06 -> Leap Year Check

checking_year = 2028
result_07 = 'Leap Year!' if (checking_year % 4 == 0 and (
    checking_year % 100 != 0 or checking_year % 4 == 0)) else 'Not Leap year'
# print(result_07)

########
# Exercise 07 -> FizzBuzz

checking_num_x = 22
result_08 = 'FizzBuzz' if (checking_num_x % 3 == 0 and checking_num_x % 5 == 0) else (
    'Fizz' if checking_num_x % 3 == 0 else 'Buzz' if checking_num_x % 5 == 0 else str(checking_num_x))
# print(result_08)

########
# Exercise 08 -> Grade System

checking_mark = 35
result_09 = 'A' if checking_mark >= 80 else (
    'B' if checking_mark >= 60 else ('C' if checking_mark >= 40 else 'F'))
# print(result_09)
