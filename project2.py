print("welcome to tip calulator")
bill = 153.45
print(" total bill is $100")
tip = float(input("how much would you like to give? 10, 12, or 15?\n")) 
bill_split =int(input("how many people to split the bill?\n"))
result = tip / 100 * bill + bill
result/=bill_split
final=round(result,2)
print(f"your total is{final}")




print("welcome to tip calulator")
bill = 124.56
print(" total bill is $124.56")
tip = input(print("how much would you like to give? 10, 12, or 15?"))
bill_split = input(print("how many people to split the bill?"))
result = int(tip) / 100 * bill
final_result = result + bill
final_result /= int(bill_split)
print(f"your total is{final_result}")