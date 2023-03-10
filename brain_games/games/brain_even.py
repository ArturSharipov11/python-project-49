from random import randint


EVEN_MIN_VALUE = 1
EVEN_MAX_VALUE = 111


RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_question_and_answer():
    rand = randint(EVEN_MIN_VALUE, EVEN_MAX_VALUE)
    answer = 'yes' if is_even(rand) else 'no'
    question_and_answer = (rand, answer)
    return question_and_answer


def is_even(number):
    return number % 2 == 0
