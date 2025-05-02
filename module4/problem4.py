# Ask for user age
age = int(input("What is your age? "))

if age < 13:
    print("You can watch G-rated movies.")
elif age <= 17:
    print("You can watch PG-13 movies.")
else:
    print("You can watch R-rated movies.")
