from random import randint, choice


from brain_games.engine import MAX_VALUE, MIN_VALUE


RULES = 'What is the result of the expression?'


def get_question_and_answer():
    random1 = randint(MIN_VALUE, MAX_VALUE)
    random2 = randint(MIN_VALUE, MAX_VALUE)
    oper = choice(['+', '*', '-'])
    if oper == '+':
        question = f'{random1} + {random2}'
        answer = random1 + random2
    elif oper == '-':
        question = f'{random1} - {random2}'
        answer = random1 - random2
    elif oper == '*':
        question = f'{random1} * {random2}'
        answer = random1 * random2
    return question, str(answer)
