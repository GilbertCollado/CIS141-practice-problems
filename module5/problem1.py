#Prompt the user for a positive integer n. Use a while loop to sum all the integers from 1 up to n. Print the final sum.

n = int(input("Enter a positive integer: "))
counter = 1
total = 0
while counter <= n:
    total += counter
    counter += 1
print("The sum is:", total)
