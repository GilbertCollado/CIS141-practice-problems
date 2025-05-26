# Write a function called ferry_fare(age, vehicle) that calculates the Washington State Ferry fare based on age and whether the person has a vehicle.
def ferry_fare(age, vehicle):
    if age <= 18:
        return 0
    elif age >= 65:
        return 15 if vehicle else 5
    else:
        return 20 if vehicle else 10
