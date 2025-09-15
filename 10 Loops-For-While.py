#Introduction to loops in Python
#For loop in a list example

#This loop will iterate through each item in the list and print a message

fruits = ["apples", "bananas", "cherries"]  #List of fruits

for fruit in fruits:                        #For each fruit in the list
    print("I like to eat " + fruit)         #Print a message with the fruit name


#While loop example
#This loop will continue to run until the condition is no longer true

count = 0                                   #Initialize count variable

while count < 5:                            #While count is less than 5
    print("Count is: " + str(count))        #Print the current count
    count += 1                              #Increment count by 1
    
print("Loop has ended.")                    #Print message after loop ends