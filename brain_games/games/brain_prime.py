from random import randint


PRIME_MIN_VALUE = 1
PRIME_MAX_VALUE = 123
RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_question_and_answer():
    ran = randint(PRIME_MIN_VALUE, PRIME_MAX_VALUE)
    question_and_answer = (ran, is_prime(ran) and 'yes' or 'no')
    return question_and_answer


def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num // 2):
        if num % i == 0:
            return False
    return True
