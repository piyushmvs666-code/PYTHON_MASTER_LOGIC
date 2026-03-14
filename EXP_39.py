# 8. Take an integer (1–9999) and check if the sum of its digits is greater than the product of its digits.
num = int(input("Enter an integer (1–9999): "))
digits = [int(d) for d in str(num)]
digit_sum = sum(digits)
digit_product = 1
for d in digits:
    digit_product *= d

if digit_sum > digit_product:
    print("The sum of the digits is greater than the product of the digits.")
elif digit_sum < digit_product:
    print("The product of the digits is greater than the sum of the digits.")
else:
    print("The sum and product of the digits are equal.")
