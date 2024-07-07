import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


#easy type without shuffle
#password=""
#password1=""
#password2=""
#for i in range(0,nr_letters,1):
 #   password+=random.choice(letters)
#print("the random letters for your password is "+password)    
#for i in range(0,nr_symbols,1):
#    password1+=random.choice(symbols)
#print("the random symbol for your password is "+password1)
#for i in range(0,nr_numbers,1):
 #   password2+=random.choice(numbers) 
  #  print("the random numbers for your password is "+password2)
#print("you password is "+password+password1+password2)


#hard  type with shuffle
password_list=[]
for i in range(0,nr_letters,1):
    password_list+=random.choice(letters)
for i in range(0,nr_symbols,1):
    password_list+=random.choice(symbols)
for i in range(0,nr_numbers,1):
    password_list+=random.choice(numbers)

print(password_list) 
random.shuffle(password_list)
print(password_list)  
char=""
for ni in password_list:
    char+=ni
print(char) 