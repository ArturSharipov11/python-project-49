import prompt


ROUNDS = 3


def start_game(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.RULES)
    for i in range(ROUNDS):
        (question, answer) = game.get_question_and_answer()
        print(f"Question: {question}")
        user_answer = prompt.string('Your answer: ')
        if user_answer == answer:
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(."
                  f"Correct answer was '{answer}'."
                  f"\nLet's try again, {name}!")
            exit()
    print(f"Congratulations, {name}!")
