# Ask for order total
order_total = float(input("Enter your order total: "))

# Calculate final cost
if order_total < 50:
    total_cost = order_total + 5
else:
    total_cost = order_total

print("Total cost including shipping: $" + str(total_cost))
