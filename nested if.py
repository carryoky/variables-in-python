#Quiz
winning_number=10
number=int(input("Guess a number:"))
if number==winning_number:
  print("YOU WIN!!!!")
else:
  if number>winning_number:
    print("Too High")
  else:
    print("Too Low")