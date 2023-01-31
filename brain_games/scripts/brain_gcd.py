import prompt


from random import randint


from random import choice

import math


def brain_gcd():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print('Find the greatest common divisor of given numbers.')
    i = 1
    while i <= 3:
        x = randint(1,100)
        y = randint(1, 100)
        print(f'Question: {x} {y}')
        answer = prompt.string('Your answer: ')
        if  answer == str(math.gcd(x, y)):
            print('Correct!')
            i += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer were '{math.gcd(x, y)}'.\nLet's try again, {name}!")
            break

        if i > 3:
            print(f"Congratulations, {name}!")

def main():
    brain_gcd()


if __name__ == '__main__':
    main()
