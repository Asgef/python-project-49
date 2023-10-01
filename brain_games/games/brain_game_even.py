import random
import prompt

show_rules = 'Answer "yes" if the is even, otherwise answer "no".'


def ask_question_even():
    number = random.randint(1, 100)
    print(f'Question: {number}')
    return number


def request_response_even():
    return prompt.string('Your answer: ')


def process_data_even(question, answer):
    if question % 2 == 0 and answer == 'yes':
        return True, 'yes',
    elif question % 2 != 0 and answer == 'no':
        return True, 'no',
    else:
        return False, invert_answer(answer)


def invert_answer(answer):
    if answer == 'yes':
        return "'no'"
    elif answer == 'no':
        return "'yes'"
    else:
        return "'yes' or 'no'"
