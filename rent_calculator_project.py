print("**************Welcome to python rent calculator project*************")
rent=int(input("Enter hostel/flat rent: "))
food=int(input("Enter amount of food ordered: "))
electricity_spend=int(input("Enter total unit of electricity spend: "))
charge_per_unit=int(input("Enter the charge per unit: "))
gass_bill=int(input("Enter gass bill: "))
internet_bill=int(input("Enter internet bill: "))
electric_bill=electricity_spend*charge_per_unit
total_payment=rent+food+electric_bill+gass_bill+internet_bill
n=int(input("Enter the number of people living in flat/hostel: "))
rent_per_person=total_payment/n
print("Total rent summary","\n")
print("Total rent is:",total_payment,"\n","Rent per person is:",round(rent_per_person,2))