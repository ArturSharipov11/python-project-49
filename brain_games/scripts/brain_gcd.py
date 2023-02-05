import prompt


from random import randint


import math


def brain_gcd():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print('Find the greatest common divisor of given numbers.')
    i = 1
    while i <= 3:
        x = randint(1, 100)
        y = randint(1, 100)
        print(f'Question: {x} {y}')
        ans = prompt.string('Your answer: ')
        b = math.gcd(x, y)
        if ans == str(b):
            print('Correct!')
            i += 1
        else:
            print(f"'{ans}' is wrong answer ;(. Correct answer were '{b}'.")
            print(f"Let's try again, {name}!")
            break
        if i > 3:
            print(f"Congratulations, {name}!")


def main():
    brain_gcd()


if __name__ == '__main__':
    main()
