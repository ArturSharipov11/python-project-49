import prompt


from random import randint


def brain_even():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 1
    while i <= 3:
        r = randint(1, 1000)
        print(f'Question: {r}')
        ans = prompt.string('Your answer: ')
        if (r % 2 == 0 and ans == 'yes') or (r % 2 == 1 and ans == 'no'):
            i += 1
            print('Correct!')
        if (r % 2 == 0 and ans != 'yes'):
            print(f"'{ans}' is wrong answer ;(. Correct answer was 'yes'.")
            print(f"Let's try again, {name}!")
            break
        if (r % 2 == 1 and ans != 'no'):
            print(f"'{ans}' is wrong answer ;(. Correct answer was 'no'.")
            print(f"Let's try again, {name}!")
            break
        if i > 3:
            print(f'Congratulations, {name}!')


def main():
    brain_even()


if __name__ == '__main__':
    main()
