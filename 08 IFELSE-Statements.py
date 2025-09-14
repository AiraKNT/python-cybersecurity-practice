number = int(input("Enter a number between 1 and 10: "))

if number > 4 and number < 10:
    print("Why so much?")

elif number < 4 and number > 0:    
    print("Why so little?")

elif number == 4:
    print("Perfect!")

else:
    print("Error: Invalid input")  