import random

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
           "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
symbols = ["#", "$", "%", "^", "&", ">", "(", ")", "-", "=", "_", "+", "[", "/", "!", ";", "<"]

print("""Welcome to Mazonia's password generator!\n
############################################################################################################\n
Kindly answer the questions that follow!\n
############################################################################################################\n""")
nl = int(input("How many letters do you want to be in your password? \n"))
ns = int(input("How many symbols do you want to be in your password? \n"))
nn = int(input("How many numbers do you want to be in your password? \n"))
pass_sum = nl + ns + nn
password = []
for char in range(1, nl + 1):
    password += random.choice(letters)

for char in range(1, ns + 1):
    password += random.choice(symbols)

for char in range(1, nn + 1):
    password += random.choice(numbers)

print(password)
random.shuffle(password)
print(password)

original_pass = ""
for char in password:
    original_pass += char

print(f"Your password is: {original_pass}")

