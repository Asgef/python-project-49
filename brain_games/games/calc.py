import random
import operator

RULE = 'What is the result of the expression?'


def ask_question():
    number_1 = random.randint(1, 100)
    number_2 = random.randint(1, 100)
    operators = ['+', '-', '*']
    expression_operator = random.choice(operators)
    expression = f'{number_1} {expression_operator} {number_2}'
    correct_answer = calc_expression(number_1, number_2, expression_operator)
    return expression, str(correct_answer)


def calc_expression(number_1, number_2, expression_operator):
    get_operator = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul
    }
    op = get_operator[expression_operator]
    elem = op(number_1, number_2)
    return elem
