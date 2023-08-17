
# Prompt the user for input
hours_str = input("Enter hours: ")
rate_str = input("Enter rate per hour: ")

# Convert the input strings to numbers
hours = float(hours_str)
rate = float(rate_str)

# Calculate the gross pay
if hours <= 40:
    gross_pay = hours * rate
else:
    regular_pay = 40 * rate
    overtime_hours = hours - 40
    overtime_pay = overtime_hours * rate * 1.5
    gross_pay = regular_pay + overtime_pay

print("Gross pay:", gross_pay)