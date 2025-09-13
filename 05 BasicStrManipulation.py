username = "Aira"
print(username)

username = "Aira "
print("Welcome ", username)             #it prints "Welcome  Aira "
print("Welcome " + username)            #it prints "Welcome Aira ", this is an example con concatenating

print(username*10)                      #prints "Aira " 10 times due to the multiplication

print(len(username))                    #prints the length of the username value, it should display the number 5

password = "password"
masked_password = "*" * len(password)   #prints "*" based on the value of the lenght of password
print(password)
print(masked_password)

text = "Cybersecurity"
first_char = text[0]
print(first_char)                       #prints only the character from string index 0 which is C from Cybersecurity

slicestring = text[0:5]
print(slicestring)                      #prints only the string from slicestring between index 0 to 5 showing only Cyber