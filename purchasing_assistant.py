"""
Program Name: Small-Business Purchasing Assistant
Name: Lynn Best
Date: August 23, 2026

Purpose: This program helps a small-business owner order items that are sold in 12-unit cases. The user enters the number of individual units needed and the price per unit. The program determines how many full cases must be ordered, calculates the subtotal, loyalty discount, handling fee, sales tax, and final total, and prints a receipt with a confirmation code.

I can explain every line of this program.
"""

import math

# Symbolic constants used for the purchasing calculations.
CASE_SIZE = 12
SALES_TAX_RATE = 0.07
LOYALTY_DISCOUNT_PERCENT = 4
HANDLING_FEE = 3
INITIALS_SEED = 'L'

print("=== Small-Business Purchasing Assistant ===")

# Get the purchasing information from the user.
# int() is used because the number of units must be a whole number.
units_needed = int(input("Enter number of units needed: "))

# float() is used because the price can include cents.
price_per_unit = float(input("Enter price per unit: "))

# math.ceil() rounds a partial case up to a full case.
# Using // would truncate the fractional part and could order too few cases.
cases_to_order = math.ceil(units_needed / CASE_SIZE)

# Calculate the quantities and purchase amounts.
units_ordered = cases_to_order * CASE_SIZE
subtotal = units_ordered * price_per_unit
discount = subtotal * (LOYALTY_DISCOUNT_PERCENT / 100)
taxable = subtotal - discount + HANDLING_FEE
tax = taxable * SALES_TAX_RATE
total = taxable + tax

# Create the confirmation code by shifting the initial three positions forward in the alphabet.
confirmation_letter = chr(ord(INITIALS_SEED) + 3)
confirmation_code = confirmation_letter + "-" + str(cases_to_order)

# Display the completed receipt.
print("\nUnits needed:\t\t" + str(units_needed))
print("Cases to order:\t\t" + str(cases_to_order) + "\t(" + str(units_ordered) + " units)")
print("Subtotal:\t\t$" + str(round(subtotal, 2)))
print("Loyalty discount:\t-$" + str(round(discount, 2)))
print("Handling fee:\t\t+$" + str(HANDLING_FEE) + ".00")
print("Tax:\t\t\t$" + str(round(tax, 2)))
print("-------------------------------")
print("TOTAL:\t\t\t$" + str(round(total, 2)))
print("Confirmation code:\t" + confirmation_code)
