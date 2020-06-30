import random

CAP = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
low = CAP.lower()
num = "0123456789"
symboles = "!@#$%^&*?/><."

raw = CAP + low + num + symboles

len = int(input("Enter the length of the password : "))

# password = ''.join(random.choice(raw) for i in range(len))
password = ''.join(random.sample(raw, len))

print(f"Your password is {password} ")
