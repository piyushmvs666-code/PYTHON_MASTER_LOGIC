# *Question: Find the second largest number in a list without using `sort()`*
def second_largest(nums):
    if len(nums) < 2:
        return None
    
    first = second = float('-inf')
    
    for num in nums:
        if num > first:
            second = first
            first = num
        elif first > num > second:
            second = num
            
    return second if second != float('-inf') else No
