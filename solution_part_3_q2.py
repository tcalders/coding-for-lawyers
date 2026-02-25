# see slides for diagram - example 2

print("Deciding if a term in a bilateral contract is unfair in the sense of Directive 93/13")

applicable=True
unfair=True

q1=input("Is one party to the contract a customer ? ")
if q1=="n":
  applicable=False
else:
  q2=input("Is the other party to the contract a customer ? ")
  if q2=="y":
    applicable=False
  else:
    q3=input("Is the term individually negotiated ? ")
    if q3=="y":
      applicable=False
    else:
      q4=input("Does the term fall within the categories listed in the Annex to the directive ? ")
      if q4=="n":
        q5=input("Is the term contrary to the requirement of good faith and does it cause a significant imbalance in the parties' rights and obligations arising under the contract, to the detriment of the consumer ? ")
        if q5=="n":
          unfair=False
if not applicable:
  print("The directive does not apply to this contract")
elif unfair:
  print("The term is unfair in the sense of Directive 93/13")
else:
  print("The term is not unfair in the sense of Directive 93/13")
  
    