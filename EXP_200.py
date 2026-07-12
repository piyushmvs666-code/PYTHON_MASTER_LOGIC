# Write a Python program to print the next number in this series*  
`8, 13, 21, 34, 55, ?`
  def next_in_series(series):
    # For Fibonacci-type series
    return series[-1] + series[-2]

# Given series
series = [8, 13, 21, 34, 55]

next_num = next_in_series(series)
series.append(next_num)

print("Series:", series)
print("Next number is:", next_num)
