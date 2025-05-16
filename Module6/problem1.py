# Sum of all even numbers in a list
numbers = [1, 4, 7, 10, 15, 22]
even_sum = 0
for num in numbers:
    if num % 2 == 0:
        even_sum += num
print("Sum of even numbers:", even_sum)
