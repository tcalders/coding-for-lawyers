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
years=int(input("for how many years do you want the table: "))

maxm=years*12
outstanding=loan
month=1
paid=0
while outstanding>0 and month<=maxm:
  outstanding=outstanding*(1+interest)
  if payment>outstanding:
    thismonthspayment=outstanding
  else:
    thismonthspayment=payment
  paid=paid+thismonthspayment
  outstanding=outstanding-thismonthspayment
  print("outstanding loan after",month, "months:",outstanding)
  month+=1

print("total paid",paid)
