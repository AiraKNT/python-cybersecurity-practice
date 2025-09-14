email = "aira@security.com"
domain = email.split('@')[1]     #splits the email value at the character @ and takes the second part
print(domain)                    #prints the domain part of the email value

print(email.split('@')[0])       #prints the first part of the email value

url = "https://www.security.com/resources/file/index.html"
file_name = url.split('/')[-1]    #splits the url value at the character / and takes the last part
print(file_name)                  #prints the file name part of the url value

print("Username:", email[:email.index("@")])   #prints the username part of the email value using slicing
print("Domain:", email[email.index("@")+1:])  #prints the domain part of the email value using slicing