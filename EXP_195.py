# Generate a random integer between 1 and 100.
  import random
  def random_int():
    try:
        value = random.randint(1, 100) 
        print("Random Integer:", value)
    except Exception as e:
        print("Error:", e)

random_int()
