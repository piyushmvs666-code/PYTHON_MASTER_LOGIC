# Write a Python function that takes a list of elements as an input and returns a dictionary detailing how many times each unique item appears.
 def count_element_frequency(elements):
    frequency_dict = {}
    
    for item in elements:
        if item in frequency_dict:
            frequency_dict[item] += 1
        else:
            frequency_dict[item] = 1
            
    return frequency_dict
