import random

def shuffle(string):
    tempList = list(string)
    random.shuffle(tempList)
    return ''.join(tempList)

uppercaseLetter1 = chr(random.randint(65,90))
uppercaseLetter2 = chr(random.randint(65,90))
uppercaseLetter3 = chr(random.randint(65,90))
lowercaseLetter1 = chr(random.randint(97,122))
lowercaseLetter2 = chr(random.randint(97,122))
lowercaseLetter3 = chr(random.randint(97,122))
lowercaseLetter4 = chr(random.randint(97,122))
symbol = chr(random.randint(33,47))
number = chr(random.randint(48,57))

password = uppercaseLetter1 + uppercaseLetter2 + uppercaseLetter3 + lowercaseLetter1 + lowercaseLetter2 + lowercaseLetter3 + lowercaseLetter4
password = shuffle(password) + number + symbol

print("Your password is " + password)