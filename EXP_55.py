# 3. Check if a number is an Armstrong number
num = int(input("Enter a number: "))
power = len(str(num))
sum_of_powers = 0

for digit in str(num):
    sum_of_powers += int(digit) ** power

if sum_of_powers == num:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")
