import random
import time
passlen = int(input("Password Length: "))
s="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789?><,.:;}]{[|"
upassword = "".join(random.sample(s, passlen))
print(upassword)
print("------------------------")

# importing random
# taking input from user
# storing alphabet letter to use thm to crack password
password = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j','k', 
            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't','u','v', 
          'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K' ,'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '?', '>', '<',',','.',':',';','}',']','{','[','|',]

# initializing an empty string
guess = ""

guesses = 0
# using while loop to generate many passwords untill one of
starttime = time.time()
# them does not matches user_pass
while (guess != upassword):
    guess = ""
    # generating random passwords using for loop
    for letter in range(len(upassword)):
        guess_letter = password[random.randint(0, 72)]
        guess = str(guess_letter) + str(guess)
        guesses=guesses+1
    # printing guessed passwords
            
# printing the matched password
endtime = time.time()
total = endtime-starttime
print("Your password is: ", guess)
print(guesses)
print(total)
