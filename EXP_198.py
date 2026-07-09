# Find Two Numbers That Add Up to a Target.
  def two_sum(nums: list[int], target: int) -> list[int]
    for current_index, num in enumerate(nums):
        complement = target - num
        if complement in seen_numbers:
            return [seen_numbers[complement], current_index]     
    return []  
