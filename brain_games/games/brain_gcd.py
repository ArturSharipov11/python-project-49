from random import randint


from brain_games.engine import MIN_VALUE, MAX_VALUE


import math


RULES = 'Find the greatest common divisor of given numbers.'


def get_question_and_answer():
    rand1 = randint(MIN_VALUE, MAX_VALUE)
    rand2 = randint(MIN_VALUE, MAX_VALUE)
    question_and_answer = (f'{rand1} {rand2}', str(get_gcd(rand1, rand2)))
    return question_and_answer


def get_gcd(num1, num2):
    yeah = math.gcd(num1, num2)
    return yeah
