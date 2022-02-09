print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip_amount = int(input("How much tip would you like to give? 10, 12, or 15? "))
no_of_people = int(input("How many people to split the bill? "))

bill_with_tip = bill + (bill*tip_amount)/100
each_person_bill = round(bill_with_tip/no_of_people,2)

print(f"Each person should pay {each_person_bill}")