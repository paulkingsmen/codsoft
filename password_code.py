import random
length = int(input("How long would you like your password to be ? "))

password = ""  # Initialize an empty string for the password
ALPHAS = ['z','x','c','v','b','n','m','a','s','d','f','g','h','j','k','l','q','w','e','r','t','y','u','i','o','p','Z','X','C','V','B','N','M','A','S','D','F','G','H','J','K','L','Q','W','E','R','T','Y','U','I','O','P']
symbols = ["!","@","#","$","%","&","*","_"]

# Loop until the password length = user input
while len(password) < length:
    # Add 5 random alphabets
    for x in range(5):
        password += ALPHAS[random.randint(0, 51)]
    # Add 3 random symbols
    for x in range(3):
        password += symbols[random.randint(0, 7)]

# Shuffle the password to make it more random
password_list = list(password)
random.shuffle(password_list)
password = ''.join(password_list)

print(password)
