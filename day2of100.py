print('Welcome to the tip calculator')
bill = float(input("what was the total bill?"))
tip = int(input("how much tip would you like to give?10,12 or 15%"))
people = int(input("how many people to split the bill?"))
bill_with_tip = tip/100*bill+bill
bill_per_person=bill_with_tip/people
final_bill=round(bill_per_person,2)
print(f"the total bill is {final_bill}")