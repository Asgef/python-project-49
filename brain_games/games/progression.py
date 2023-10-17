import random

RULE = 'What number is missing in the progression?'


def ask_question():
    # number of terms of an arithmetic progression
    n = 10

    # random first element of an arithmetic progression
    a = random.randint(1, 20)

    # random difference between terms of an arithmetic progression
    d = random.randint(1, 10)
    progression = generate_progression(n, a, d)
    char = '..'
    random_element_i = random.randint(1, 9)
    correct_answer = progression[random_element_i]
    progression[random_element_i] = char
    question_str = ' '.join(map(str, progression))
    return question_str, str(correct_answer)


def generate_progression(n, a, d):
    progression = [a + d * i for i in range(n)]
    return progression
