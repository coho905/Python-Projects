import random
passlen = int(input("Password Length: "))
s="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789?><,.:;}]{[|\+-)(*&^%$#@!"
password = "".join(random.sample(s, passlen))
print(password)
