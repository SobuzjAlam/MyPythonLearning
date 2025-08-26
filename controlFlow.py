# basic control flow

"""
Ternary operators -> 
    Conditional expressions, It evaluates a condition and returns one of two values.
    ***[value_if_true if condition else value_if_false]**
"""

# Exercise 01 -> Even or Odd

cheking_num = 7
result_01 = 'Even' if cheking_num % 2 == 0 else 'Odd'
# print(result_01)

#########################

cheking_list = list(range(1, 101))


def checkingOddEvenList(list):
    odd_list = []
    even_list = []
    for i in list:
        if ('Even' if i % 2 == 0 else 'Odd') == 'Odd':
            odd_list.append(i)
        else:
            even_list.append(i)

    return (f'ODD List: {odd_list} \nEVEN List: {even_list}')


result_02 = checkingOddEvenList(cheking_list)
# print(result_02)

########
# Exercise 02 -> Positive, Negative, or Zero

cheking_classification = -3
result_03 = 'Positive' if cheking_classification > 0 else (
    'Zero' if cheking_classification == 0 else 'Negative')
# print(result_03)

########
# Exercise 03 -> Adult or Minor
