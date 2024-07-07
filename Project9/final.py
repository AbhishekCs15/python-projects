

import os.system
from art import logo
print(logo)

def highest_bider(dict1):
    final_amount = 0
    for bidder in dict1:
        amount = dict1[bidder]
        if amount > final_amount:
            final_amount = amount
    print(f"the winner is {bidder} with the bit of {final_amount}")


dict={}
bit = False
while not bit:
    no = input("enter your name?: ")
    bo = int(input("enter a bid price: $"))
    dict[no] = bo
    vari = input("are there any other to bid,type 'yes' if so else 'no' ").lower()

    if vari == "no":
        bit = True
    elif vari == "yes":
       print("bye")
highest_bider(dict)
