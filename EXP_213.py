#  Given a list of items, write a Python script to swap the very first element with the very last element.
   def swap_first_last(my_list):
    # Check if the list has at least two elements to swap
    if len(my_list) >= 2:
        # Pythonic assignment trick to swap variables
        my_list[0], my_list[-1] = my_list[-1], my_list[0]
    return my_list
