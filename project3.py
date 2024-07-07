print("Welcome to treasure island")
print("Your mission is to find treasure")
choice=input('do you want to go "left" or "right".').lower()
if choice=="right":
  print("game over")
elif choice=="left":
  choice1=input("you\'ve an pond! do you want to wait for BOAT or SWIM").lower()
  if choice1=="swim":
    print("game over because of snakes in the pond")
  elif choice1=="wait":
    choice2=input("which door do you choose RED BLUE or GREEN").lower()
    if choice2=="red":
       print("game over")
    elif choice2=="blue":
       print("game over")
    elif choice2=="green":
       print("game won")
    else:
     print("valid input")
  else:
    print("valid input")
else:
  print("valid input")
    