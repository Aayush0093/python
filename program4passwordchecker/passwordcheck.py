username = input("What's your username ? ")
password = input("What's your password ? ")

password_length = len(password)
hidden_password = '*' * password_length

print(f"{username} your password is {hidden_password} and is {password_length} characters long.")