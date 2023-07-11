# def is_even (number):
#     if number % 2 == 0:
#         return True
#     else:
#         return False

# print(is_even(6))
# print(is_even(7))


y = 7
u = 8
print(y+u)

# def is_even (number):
#     if number % 2 == 0:
#         return True
#     else:
#         return False
# var = int(input("Enter Number"))

# print(is_even(input(var)))
# print(is_even(input("second number")))

# print(input( is_even()))

# is_even(print(input()))

# is_even() = print()

# even = "even"
# odd = "odd"

# def is_even(number):
#     if number % 2 == 0:
#         return "even"
#     else:
#         return "odd"

# # Prompt the user to enter a number
# number = int(input("Enter a number: "))

# # Call the is_even function and print the result
# print(is_even(number))



# import datetime

# # Set the target date and time
# target_date = datetime.datetime(2023, 6, 29, 0, 0)

# # Get the current date and time
# current_date = datetime.datetime.now()

# # Calculate the time difference
# time_difference = target_date - current_date

# # Extract the remaining days, hours, and minutes
# remaining_days = time_difference.days
# remaining_hours = time_difference.seconds // 3600
# remaining_minutes = (time_difference.seconds // 60) % 60

# # Check if it's already the target time
# if time_difference.total_seconds() <= 0:
#     print("Happy Eid al-Adha, username!")
# else:
#     # Request username
#     username = input("Please enter your username: ")

#     # Print the remaining time
#     print("Days:", remaining_days)
#     print("Hours:", remaining_hours)
#     print("Minutes:", remaining_minutes)
#     print("Happy Eid al-Adha, " + username + "!")



import datetime

# Set the target date and time
target_date = datetime.datetime(2023, 6, 28, 0, 0)

# Get the current date and time
current_date = datetime.datetime.now()

# Calculate the time difference
time_difference = target_date - current_date

# Extract the remaining days, hours, and minutes
remaining_days = time_difference.days
remaining_hours = time_difference.seconds // 3600
remaining_minutes = (time_difference.seconds // 60) % 60

# Check if it's already the target time
if time_difference.total_seconds() <= 0:
    username = input("Please enter your username: ")
    print(username, "Happy Eid al-Adha!")
else:
    # Print the remaining time
    username = input("Please enter your username: ")
    print("Days:", remaining_days)
    print("Hours:", remaining_hours)
    print("Minutes:", remaining_minutes)
    print(username ,",", "It's not Eid day yet. Hang in there! Eid remains ", remaining_days, "days")
