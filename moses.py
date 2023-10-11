print("WELCOME TO THE BILL CALCULATOR!!!")
bill =float(input("what is the bill for today?\n"))
tip = int(input("what percentage will you give as tip?\n10, 12, 15, 20?\n"))/100
total_bill= round((1 + tip) * bill,2)
opt = input("Are you rooting the whole bill?\n Type Y for YES or N for NO.\n").lower()
if opt == "y":
  print(f"Your bill for today is {total_bill}")
elif opt == "n":
  number_of_people= int(input("how many ways do you want to spilt today's bill?\n"))
  part_bill= round(total_bill/number_of_people,2)
  print(f"Each person should pay ${part_bill}")
else:
  print("Wrong input. Let's try again")
