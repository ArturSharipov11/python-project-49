from random import randint


from brain_games.engine import MIN_VALUE, MAX_VALUE
RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_question_and_answer():
    ran = randint(MIN_VALUE, MAX_VALUE)
    question_and_answer = (ran, is_prime(ran))
    return question_and_answer


def is_prime(num):
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1
    if count == 2:
        return 'yes'
    elif count != 2:
        return 'no'
