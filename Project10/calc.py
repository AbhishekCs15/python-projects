from art import logo
print(logo)
def add(n1 , n2):
    return n1 + n2
def sub(n1 , n2):
    return n1 - n2
def mul(n1 , n2):
    return n1 * n2
def div(n1 , n2):
    return n1 / n2

dic = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
}
def calculator():
    n1 = float(input("enter the first no"))
    for operation in dic:
        print(operation)

    user_option = True
    while user_option:
        symbol = input("enter the above symbol operation you want to perform")
        n2 = float(input("enter the secound no"))
        n3 = dic[symbol]
        answer = n3(n1, n2)
        print(f"{n1} {symbol} {n2}  = {answer}")
        user= input("type 'yes' to add new number to answer or 'no' to exit or 'new' for fresh start").lower()
        if user == "yes":
            n1 = answer
        elif user == "new":
            calculator()
        elif user == "no":
            user_option = False
            print("thanks for using")
        else:
            user_option = False
            print("enter the correct input")
            calculator()


calculator()





