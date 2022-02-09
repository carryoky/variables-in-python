#Quiz
salary=int(input("Enter salary:"))
years=int(input("Enter years:"))
if years>10:
  print("Net salary is",(0.1*salary+salary))
elif years>=6 and years<=10:
  print("Net salary is",(0.08*salary+salary)) 
else:
  print("Net salary is",(0.05*salary+salary))
