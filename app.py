import random

numbers = 5 #input('How many passwords needed: ')
letters = '1234567890-=!@#$%^&*()_+asdfghjkl:"zxcvbnm<>?ASDFGHJKL;ZXCVBNM,./QWERTYUIOP[]{}\''
length = 9 #input('What is the length of password: ')

for x in range(int(numbers)):
    pwd = ''
    print("THIS IS THE RANDOM PASSWORD GENERATOR FOR 5 NUMBERS WITH LENGTH=9")
    for _ in range(int(length)):
        pwd += random.choice(letters)
    print(pwd)
