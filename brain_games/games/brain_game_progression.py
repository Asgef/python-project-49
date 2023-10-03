import random

show_rules = 'What number is missing in the progression?'


def generate_progression():
    # number of terms of an arithmetic progression
    n = 10

    # random first element of an arithmetic progression
    a = random.randint(1, 20)

    # random difference between terms of an arithmetic progression
    d = random.randint(1, 10)

    progression = [a + d * i for i in range(n)]
    return progression


def ask_question_progression():
    char = '..'
    progression = generate_progression()
    random_element_i = random.randint(1, 9)
    element = progression[random_element_i]
    progression[random_element_i] = char
    question_str = ' '.join(map(str, progression))
    show_question = f'Question: {question_str}'
    print(show_question)
    return element


def process_data_progression(question, answer):
    if question == answer:
        return True, 0,
    else:
        return False, f"was '{question}'"
