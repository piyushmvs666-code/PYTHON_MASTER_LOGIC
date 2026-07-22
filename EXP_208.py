# Python Code for Asking a User a Question.
  # 1. Ask a question and save the user's response
user_name = input("What is your name? ")

# 2. Ask a question that requires a number response
# Note: input() always saves text, so we convert it to an integer using int()
user_age = int(input("How old are you? "))

# 3. Print the results using an f-string
print(f"Hello {user_name}! Next year you will be {user_age + 1} years old.")
