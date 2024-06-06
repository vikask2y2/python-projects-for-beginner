import random
import string

pass_len = 12
passValues = string.ascii_letters + string.digits + string.punctuation

password = ""
for i in range (pass_len):
    password += random.choice(passValues)

print("Your password:", password)
