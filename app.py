import random

print("**********PASSWORD GENERATOR**********")
while True:
    lettersL = "abcdefghijklmnopqrstuvwxyz"
    lettersU = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "1234567890"
    symbols = "!@#$%^&*()_+="
    allowedValues = ""
    generatedPassword = ""


    print("**************************************")
    print("[1] Generate Password")
    print("[2] Exit")

    try:
        choice = int(input())
    except ValueError:
        choice = 0
    if(choice == 1):
        try:
            length = int(input("Enter the lenght: "))
        except ValueError:
            length = 0
        if length <= 0:
            print("Password length must be at least one character long\n")
        else:
            includeLettersL = input("Do you want to include lowercase letters? [Y/N] (default: y): ")
            if(includeLettersL == "Y" or includeLettersL == "y" or includeLettersL == ""):
                allowedValues += lettersL
                LetL = True
            else:
                LetL = False
                allowedValues += ""
            includeLettersU = input("Do you want to include uppercase letters? [Y/N] (default: y): ")
            if(includeLettersU == "Y" or includeLettersU == "y" or includeLettersU == ""):
                allowedValues += lettersU
                LetU = True
            else:
                LetU = False
                allowedValues += ""
            includeNums = input("Do you want to include numbers? [Y/N] (default: y): ")
            if(includeNums == "Y" or includeNums== "y" or includeNums == ""):
                allowedValues += numbers
                Num = True
            else:
                Num = False
                allowedValues += ""
            includeSyms = input("Do you want to include symbols? [Y/N] (default: y): ")
            if(includeSyms == "Y" or includeSyms == "y" or includeSyms == ""):
                allowedValues += symbols
                Syms = True
            else:
                Syms = False
                allowedValues += ""
            if LetL == False and LetU == False and Num == False and Syms == False:
                print("At least one parameter has to be selected\n")
            else:
                for i in range(0, length):
                    randomIndex = random.randint(0, len(allowedValues))
                    try:
                        generatedPassword += allowedValues[randomIndex]
                    except IndexError:
                        randomIndex = random.randint(0, len(allowedValues))
                        generatedPassword += allowedValues[randomIndex]
                print("Generated password:\n", generatedPassword)

    elif(choice == 2):
        break
    else:
        print("Command not found :/")
     
print("**************************************")