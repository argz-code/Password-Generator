import random
import string
len=int(input("Kindly mention the length of your password: "))
values=string.ascii_letters+string.digits+string.punctuation

password=""
for i in range(len):
    password+=random.choice(values)

print(password)