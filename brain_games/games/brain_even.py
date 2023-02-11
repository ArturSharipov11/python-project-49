from random import randint


from brain_games.engine import MIN_VALUE, MAX_VALUE


RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_question_and_answer():
    rand = randint(MIN_VALUE, MAX_VALUE)
    question_and_answer = (rand, is_even(rand) and 'yes' or 'no')
    return question_and_answer


def is_even(number):
    return number % 2 == 0
