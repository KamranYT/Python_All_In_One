import random

print("Welcome To Your Password Generator")

ch = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@$%&*().,?0123456789"

number = input("Enter Amount of passwords to generate: ")
number = int(number)

length = input("Enter Your Password Length: ")
length = int(length)

print('\nhere are your passwords: ')

for pwd in range(number):
    passwords = ''
    for c in range(length):
        passwords += random.choice(ch)
    print(passwords)