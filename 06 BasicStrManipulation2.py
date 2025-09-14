password = "      alphabet     "
print(password.strip())                #removes the spaces before and after the string value
print(password.lstrip())               #removes the spaces before the string value
print(password.rstrip())               #removes the spaces after the string value

message = "I am learning Python"
print(message.lower())                 #prints the string value in lowercase
print(message.upper())                 #prints the string value in uppercase
print(message.replace("Python", "JavaScript"))  #replaces the word Python with JavaScript

password = "P@ssw0rd"
secure_password = password.replace("P@ssw0rd", "[REDACTED]")    #print the password value as [REDACTED]
print(secure_password)
print(password)

if password.find("@") != -1:               #checks if the character @ is in the password value
    print("Valid password")