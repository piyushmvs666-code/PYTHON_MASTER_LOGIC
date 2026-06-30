# Dynamic Math Quiz (Infinitely Generated Questions)
 import random

def math_quiz():
    score = 0
    total_questions = 0
    operators = ['+', '-', '*', '/']
    
    print("Welcome to the Infinite Math Quiz! (Type 'quit' at any time to exit)")

    while True:
        num1 = random.randint(1, 20)
        num2 = random.randint(1, 20)
        op = random.choice(operators)

        if op == '/':
            num1 = num2 * random.randint(1, 10)

        question = f"What is {num1} {op} {num2}? "
        user_input = input(question).strip().lower()

        if user_input == 'quit':
            break

        try:
            user_answer = float(user_input)
        except ValueError:
            print("Invalid input! Please enter a valid number.\n")
            continue

        if op == '+':
            correct_answer = num1 + num2
        elif op == '-':
            correct_answer = num1 - num2
        elif op == '*':
            correct_answer = num1 * num2
        else:
            correct_answer = num1 / num2

        total_questions += 1
        if abs(user_answer - correct_answer) < 1e-9:
            print("Correct!\n")
            score += 1
        else:
            print(f"Incorrect. The correct answer was {correct_answer:.2f}\n")

    print(f"\nQuiz Over! You answered {score} out of {total_questions} questions correctly.")

if __name__ == "__main__":
    math_quiz()
 
