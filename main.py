"""
Author: Venzah Hamilton
Date: June 17, 2026
Summary: This will sum even and odd numbers between 5 and 15 and print out their computation
"""

# Loops through all the even numbers between 5 and 15
for even in range(6, 15, 2):
    # Loops through all the odd numbers between 5 and 15
    for odd in range(5, 15, 2):
        # Calculates the sum and prints out the calculation
        calc = even + odd
        print(even, "+", odd, "=", calc)