name="Toon"
print("Hello, my name is",name)

a=5
b=a+3
print("b is equal to",b)

if b>7:
  print("b is greater than 7")
elif b==7:
  print("b is equal to 7")
else:
  print("b is smaller than 7")

avg=float(input("Average grade ? "))
if avg < 10:
    grade="Fail"
elif avg < 14:
    grade="Pass"
elif avg < 15:
    grade="Distinction"
elif avg <17:
    grade="Cum Laude"
else:  # average >= 17
    grade="Magna Cum Laude"

print(grade)



loan=float(input("give loan amount: "))
interest=float(input("give monthly interest rate: "))
payment=float(input("monthly payment: "))
print("outstanding loan after 1 month",loan*(1+interest)-payment)

outstanding=loan
for month in range(1,10):
  outstanding=outstanding*(1+interest)-payment
  print("outstanding loan after",month, "months:",outstanding)

outstanding=loan
month=1
while month<10:
  outstanding=outstanding*(1+interest)-payment
  print("outstanding loan after",month, "months:",outstanding)
  month=month+1

