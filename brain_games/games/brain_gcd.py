from random import randint


import math


GCD_MIN_VALUE = 1
GCD_MAX_VALUE = 101


RULES = 'Find the greatest common divisor of given numbers.'


def get_question_and_answer():
    rand1 = randint(GCD_MIN_VALUE, GCD_MAX_VALUE)
    rand2 = randint(GCD_MIN_VALUE, GCD_MAX_VALUE)
    question_and_answer = (f'{rand1} {rand2}', str(get_gcd(rand1, rand2)))
    return question_and_answer


def get_gcd(num1, num2):
    yeah = math.gcd(num1, num2)
    return yeah
