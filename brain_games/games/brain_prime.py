from random import randint


rules = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def question_and_answer():
    ran = randint(1, 100)
    question = ran
    count = 0
    for i in range(1, ran + 1):
        if ran % i == 0:
            count += 1
    if count == 2:
        answer = 'yes'
    elif count != 2:
        answer = 'no'
    return question, str(answer)
