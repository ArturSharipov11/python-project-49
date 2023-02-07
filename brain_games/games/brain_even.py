from random import randint

rules = 'Answer "yes" if the number is even, otherwise answer "no".'


def question_and_answer():
    r = randint(1, 100)
    question = r
    if r % 2 == 0:
        answer = 'yes'
    elif r % 2 == 1:
        answer = 'no'
    return question, str(answer)
