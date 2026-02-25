# Change the following code:
# - Ask the user for how many years they want the table
# - Print the monthly table for that many years
# 
# Extensions:
# - Stop if the outstanding amount becomes <= 0 (HINT: use while)
# - Compute the total payment
#   Take into account that the last payment is not for the full 
#   amount, but such that the balance is exactly 0




loan=float(input("give loan amount: "))
interest=float(input("give monthly interest rate: "))
payment=float(input("monthly payment: "))
print("outstanding loan after 1 month",loan*(1+interest)-payment)

outstanding=loan
for month in range(1,10):
  outstanding=outstanding*(1+interest)-payment
  print("outstanding loan after",month, "months:",outstanding)