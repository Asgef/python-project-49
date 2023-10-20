import random
import operator

RULE = 'What is the result of the expression?'

EXPR_MIN_OPERAND = 1
EXPR_MAX_OPERAND = 100


def get_question_answer():
    number_1 = random.randint(EXPR_MIN_OPERAND, EXPR_MAX_OPERAND)
    number_2 = random.randint(EXPR_MIN_OPERAND, EXPR_MAX_OPERAND)
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
