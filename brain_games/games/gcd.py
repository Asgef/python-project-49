import random


RULE = 'Find the greatest common divisor of given numbers.'


def ask_question():
    number_1 = random.randint(1, 100)
    number_2 = random.randint(1, 100)
    expression = f'{number_1} {number_2}'
    correct_answer = find_gcd(number_1, number_2)
    return expression, str(correct_answer)


def find_gcd(number_1, number_2):
    a = number_1
    b = number_2
    while b:
        a, b = b, a % b
    return a
