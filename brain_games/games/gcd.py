import random

RULE = 'Find the greatest common divisor of given numbers.'

GCD_MIN_NUM = 1
GCD_MAX_NUM = 100


def get_question_answer():
    number_1 = random.randint(GCD_MIN_NUM, GCD_MAX_NUM)
    number_2 = random.randint(GCD_MIN_NUM, GCD_MAX_NUM)
    expression = f'{number_1} {number_2}'
    correct_answer = find_gcd(number_1, number_2)
    return expression, str(correct_answer)


def find_gcd(number_1, number_2):
    a = number_1
    b = number_2
    while b:
        a, b = b, a % b
    return a
