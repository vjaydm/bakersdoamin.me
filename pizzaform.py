size =  input("What size of pizza would you like, S,M,L")
pepperoni = input("Would u like pepperoni,Yes,No")
cheese = input("Would u like cheese on it,Yes,No")


bill = 0
if size == "S":
	bill += 150
elif size == "M":
	bill += 200
elif size == "L":
	bill += 250

if pepperoni == "Yes" and size == "S":
	bill += 20
elif pepperoni == "Yes" and size == "M":
	bill += 30
elif pepperoni == "Yes" and size == "L":
	bill += 30


if cheese == "Yes":
	bill +=10

print("Your total is $",bill)