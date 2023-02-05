import prompt


from random import randint


def brain_prime():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    index = 1
    while index <= 3:
        x = randint(1, 103)
        print(f"Question: {x}")
        answer = prompt.string('Your answer: ')
        counter = 0
        for i in range(1, x + 1):
            if x % i == 0:
                counter += 1
        if (answer == 'yes' and counter == 2) or (answer == 'no' and counter != 2):
            print('Correct!')
            index += 1
        if (counter  == 2  and answer != 'yes'):
            print(f"'{answer}' is wrong answer ;(. Correct answer was 'yes'.\nLet's try again, {name}!")
            break
        if (counter != 2 and answer != 'no'):
            print(f"'{answer}' is wrong answer ;(. Correct answer was 'no'.\nLet's try again, {name}!")
            break
        if i > 3:
            print(f'Congratulations, {name}!')

def main():
    brain_prime()


if __name__ == '__main__':
    main()
