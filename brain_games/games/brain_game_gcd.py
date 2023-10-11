import random


RULE = 'Find the greatest common divisor of given numbers.'


def ask_question(process_data_func):
    number_1 = random.randint(1, 100)
    number_2 = random.randint(1, 100)
    expression = f'{number_1} {number_2}'
    correct_answer = process_data_func(number_1, number_2)
    return expression, str(correct_answer)


def process_data(number_1, number_2):
    a = number_1
    b = number_2
    while b:
        a, b = b, a % b
    return a
