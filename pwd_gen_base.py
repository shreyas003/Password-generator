#password generator project
import random
import string


print("Welcome to the password generator:\n")
length = int(input("Enter desired password length: "))
numbersFlag = input("Do you want numbers to be used? (y/n):")
specialCharFlag = input("Do you want special characters to be used? (y/n):")

def digitsCheck(password):
    numCheck = any(c.isdigit() for c in password)
    return numCheck

def specialCheck(password):
    specialCheck = any(not(c.isdigit() or c.isalpha() or c == ' ') for c in password)
    return specialCheck

def generateFunction(length, numbersFlag, specialCharFlag):

    pwd = ''

    if(numbersFlag == 'y' and specialCharFlag == 'y'):#type 1
        while digitsCheck(pwd) != True or specialCheck(pwd) != True:
            pwd = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length))
 
    elif(numbersFlag == 'y' and specialCharFlag == 'n'):#type 2
        while digitsCheck(pwd) != True:
            pwd = ''.join(random.choices(string.ascii_letters + string.digits, k=length))

    elif(specialCharFlag == 'y'and numbersFlag == 'n' ):# type 3
        while specialCheck(pwd) !=True:
            pwd = ''.join(random.choices(string.ascii_letters + string.punctuation, k=length))

    else:#type 4
        pwd = ''.join(random.choices(string.ascii_letters, k=length))

    return pwd

print("Password is: " + generateFunction(length, numbersFlag, specialCharFlag))
print('Thanks for using')









