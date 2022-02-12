# PassGenX - A program to generate passwords and keep them safe.
import random

def main():
    menu()
    
    
def menu():
    newPassCharNum = 0
    menuMassage = "Welcome to PassGenX!\nPlease select what operation you want to execute:\n    1- Create new Pass\n    2- Encrypt existing Pass\n    3- forgot Pass [ID num required]\nYour chioce: "
    operationID = int(input(menuMassage))
    
    if operationID == 1:
        newPassLength = int(input("Please enter password lenght: "))
        NewpassGenerator(newPassLength)
    elif operationID == 2:
        existingEncrypt()
        
    """elif operationID == 3:
        forgotPass()"""
        
    
    1
    
    

def NewpassGenerator(passLength):
    lowerLetterChars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u','v', 'w', 'x', 'y', 'z']
    upperLetterChars = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    specialChars = ['!', '@', '#', '$', '%', '&', '*']
    numberChars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    newPassWord = ""
    allChars = lowerLetterChars + upperLetterChars + specialChars + numberChars
    #allChars = ''.join(allChars)
    for i in range(passLength):
        newPassWord = newPassWord + random.choice(allChars)
    
        
    
    
    
    
"""
def existingEncrypt():
     
def encryptionAlgo():
    
def forgotPass():
"""
    

if __name__ == '__main__':
    main()
    
