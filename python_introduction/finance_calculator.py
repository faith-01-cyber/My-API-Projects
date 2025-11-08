# finance_calculator.py

# Get user input
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))

# Calculate monthly savings
monthly_savings = monthly_income - monthly_expenses

# Project annual savings with 5% interest
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

# Output results
print("Your monthly savings are $", monthly_savings, sep="")
print("Projected savings after one year, with interest, is: $", projected_savings, sep="")
