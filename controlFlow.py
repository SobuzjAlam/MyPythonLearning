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
