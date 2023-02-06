from random import randint, choice


rules = 'What is the result of the expression?'


def question_and_answer():
    random1 = randint(1, 50)
    random2 = randint(1, 60)
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
