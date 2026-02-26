temp = float(input("Enter temperature: "))

if temp < 15:
    print("Cold")
elif 15 <= temp <= 30:
    print("Warm")
else:
    print("Hot")