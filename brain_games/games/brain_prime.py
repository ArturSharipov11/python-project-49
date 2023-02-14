from random import randint


from brain_games.engine import MIN_VALUE, MAX_VALUE
RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_question_and_answer():
    ran = randint(MIN_VALUE, MAX_VALUE)
    question_and_answer = (ran, is_prime(ran))
    return question_and_answer


def is_prime(num):
    if num <= 1:
        return 'no'
    for i in range(2, num // 2):
        if num % i == 0:
            return 'no'
    return 'yes'
