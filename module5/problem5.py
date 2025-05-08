#Write a program that continuously asks the user to input a number. If the user enters 0, immediately stop asking for more numbers. Otherwise, print the number they entered.

while True:
    number = int(input("Enter a number (0 to stop): "))
    if number == 0:
        print("Exiting...")
        break
    print("You entered", number)
