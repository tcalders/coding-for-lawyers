# see slides for diagram - example 1 - GDPR

q1=input("Does the data relate to a person ? ")
if q1=="y":
  # data relates to a person
  q2=input("Is the person alive ? ")
  if q2=="y":
    q3=input("Can you identify the person ? ")
    if q3=="y":
      print("Yes, the data is personal data according to GDPR")
    else:
      q4=input("Can you identify the person using an ID number, ...? ")
      if q4=="y":
        print("Yes, the data is personal data according to GDPR")
      else:
        print("No, the data is not personal data according to GDPR")
  else:
    print("No, the data is not personal data according to GDPR")
else:
  print("No, the data is not personal data according to GDPR")
