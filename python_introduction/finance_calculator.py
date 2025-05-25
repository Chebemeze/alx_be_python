monthly_income = int(input("Enter your monthly income: "))
monthly_expenses  = int(input("Enter your total monthly expenses: "))
monthly_savings = monthly_income - monthly_expenses
print("Your monthly savings are", f"${monthly_savings}.")
yearly_savings = monthly_savings * 12
projected_savings = int(yearly_savings + (yearly_savings * 0.05))
print("Projected savings after one year, with interest is:", f"${projected_savings}.")
