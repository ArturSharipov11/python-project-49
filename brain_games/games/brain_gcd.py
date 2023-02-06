from random import randint


import math


rules = 'Find the greatest common divisor of given numbers.'


def question_and_answer():
    x = randint(1, 100)
    y = randint(1, 100)
    question = '{x} {y}'
    b = math.gcd(x, y)
    answer = str(b)
