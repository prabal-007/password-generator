import random

CAP = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
low = CAP.lower()
num = str(range(0, 10))
symbole = "!@#$%^&*?/."

raw = CAP + low + num + symbole
len = int(input("Enter the length of the password : "))

password = ''.join(random.sample(raw, len))
print(f"Your password is {password} ")
