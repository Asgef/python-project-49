import random
import operator
import prompt

show_rules = 'What is the result of the expression?'


def request_response_calc():
    return prompt.integer('Your answer: ')


def ask_question_calc():
    number_1 = random.randint(1, 100)
    number_2 = random.randint(1, 100)
    operators = ['+', '-', '*']
    expression_operator = random.choice(operators)
    expression = f'Question: {number_1} {expression_operator} {number_2}'
    print(expression)
    return number_1, number_2, expression_operator


def process_data_calc(question, answer):
    get_operator = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul
    }
    op = get_operator[question[2]]
    elem = op(question[0], question[1])
    if answer == elem:
        return True, elem,
    else:
        return False, f" was '{elem}'",
