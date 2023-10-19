import random

RULE = 'What number is missing in the progression?'

MUN_TERMS = 10
MIN_FIRST_ELEMENT = 1
MAX_FIRST_ELEMENT = 20
MIN_DIFFERENCE = 1
MAX_DIFFERENCE = 10
MIN_RANDOM_INDEX = 1
MAX_RANDOM_INDEX = 9


def get_question_answer():
    n_term_sequence = MUN_TERMS
    init_term = random.randint(MIN_FIRST_ELEMENT, MAX_FIRST_ELEMENT)
    diff_members = random.randint(MIN_DIFFERENCE, MAX_DIFFERENCE)

    progression = gen_progression(n_term_sequence, init_term, diff_members)

    char = '..'
    rand_element_i = random.randint(MIN_RANDOM_INDEX, MAX_RANDOM_INDEX)
    correct_answer = progression[rand_element_i]

    progression[rand_element_i] = char
    question_str = ' '.join(map(str, progression))

    return question_str, str(correct_answer)


def gen_progression(n_term_sequence, init_term, diff_members):
    return [init_term + diff_members * item for item in range(n_term_sequence)]
