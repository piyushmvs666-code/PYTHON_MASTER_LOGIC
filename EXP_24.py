# Q4. Take 24-hour time (hours and minutes) and print whether it is AM or PM.
hour = int(input("Enter hour (0-23): "))
minute = int(input("Enter minute (0-59): "))

if hour < 12:
    print("AM")
else:
    print("PM")
