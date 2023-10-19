import random

RULE = 'Find the greatest common divisor of given numbers.'

MIN_VALUE = 1
MAX_VALUE = 100


def get_question_answer():
    number_1 = random.randint(MIN_VALUE, MAX_VALUE)
    number_2 = random.randint(MIN_VALUE, MAX_VALUE)
    expression = f'{number_1} {number_2}'
    correct_answer = find_gcd(number_1, number_2)
    return expression, str(correct_answer)


def find_gcd(number_1, number_2):
    a = number_1
    b = number_2
    while b:
        a, b = b, a % b
    return a
