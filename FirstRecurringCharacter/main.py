import approach

# Prompt the user to input the string
inputString = (input("Please enter the string:"))

# Menu
print("\nChoose your desired approach:")
print("1. Approach 1(Inefficient and inaccurate)")
print("2. Approach 2(inaccurate)")
print("3. Approach 3(Efficient and accurate)")
print("4. Execute all approaches")
print("5. Exit")

# Choice
while(True):
    try:
        choice=int(input("\nPlease select your choice:"))
    except ValueError:
        print("Wrong Input")
        continue
    if choice==1:
        approach.approach_1(inputString)
    elif choice==2:
        approach.approach_2(inputString)
    elif choice==3:
        approach.approach_3(inputString)
    elif choice==4:
        approach.approach_1(inputString)
        approach.approach_2(inputString)
        approach.approach_3(inputString)
    elif choice==5:
        break
    else:
        print("Wrong Input")


