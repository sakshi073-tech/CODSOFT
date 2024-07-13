# Password Generator Program
import string
import random

lowercase = list(string.ascii_lowercase)
uppercase = list(string.ascii_uppercase)
digits = list(string.digits)
punctuation = list(string.punctuation)

user_input = input("Specify the desired length of the Password :")

while True:
    try:
        pass_number = int(user_input)
        if pass_number < 8:
            print("Number should be at least 8.")
            user_input = input("Please, Enter Your Number Again :")
        else:
            break
    except:
       print("Please, Enter Numbers Only.")
       user_input = input("How many characters do you want  in your password ?")


entire_character = lowercase + uppercase + digits + punctuation
random.shuffle(entire_character)

password = []

password.append(random.choice(lowercase))
password.append(random.choice(uppercase))
password.append(random.choice(digits))
password.append(random.choice(punctuation))

for p in range(pass_number - 4):
    password.append(random.choice(entire_character))
    random.shuffle(password)
    generated_pass = ''.join(password)
print("Your Password is :",generated_pass)








