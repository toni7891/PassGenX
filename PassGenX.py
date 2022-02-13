# PassGenX - A program to generate passwords and keep them safe.

# Imported library's 
import random
import base64

# Global variables
dataBase_Dest = r"C:\Users\Tony\Desktop\passGen PROJECT\Encrypted_Data.txt"
validationPass_Dest = r"C:\Users\Tony\Desktop\passGen PROJECT\Admin.txt"



def main():
    keepAlive = True
    while keepAlive == True:
        keepAlive = menu()
        
    

   
def menu():
    newPassCharNum = 0
    menuMassage = """Welcome to PassGenX!
    Please select what operation do you want to execute:
    1- Create new Pass    
    2- See existing Passwords
    3- Erase Data file
    4- Exit
    Your choice: """
    operationID = int(input(menuMassage))
    
    if operationID == 1:
        newPassLength = int(input("Please enter password length: "))
        NewpassGenerator(newPassLength)
        return True
    
    elif operationID == 2:
        validationID = input("Please enter Admin Password: ")
        if validateAdmin(validationID) == True:
            decodeFile()
        elif validateAdmin(validationID) == False:
            print('Wrong admin password...\nget the Fuck out!')
        return True
        
    elif operationID == 3:
        eraseDataFile()
        return True
        
    elif operationID == 4:
        return False
        
    else: 
        print("There is no such Operation ID...")        

    

def NewpassGenerator(passLength):
    lowerLetterChars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u','v', 'w', 'x', 'y', 'z']
    upperLetterChars = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    specialChars = ['!', '@', '#', '$', '%', '&', '*']
    #special64Chars = ['+', '/']
    numberChars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    newPassWord = ""
    allChars = lowerLetterChars + upperLetterChars + numberChars + specialChars
    #allChars = ''.join(allChars)
    for i in range(passLength):
        newPassWord = newPassWord + random.choice(allChars)
    print('Your new password is: ' + newPassWord)
    inFile(encryptionAlgo(newPassWord))
    print('your password have been encrypted!')
    
    
       
def encryptionAlgo(password):
    passBytes = password.encode('ascii')
    encodedPass = base64.b64encode(passBytes)
    return encodedPass

def inFile(encoded_Data):
       fileOpen = open(dataBase_Dest, "a")
       fileOpen.write(str(encoded_Data) + '\n')
       fileOpen.close() 
       print('Your Password has been saved!')
 

def decodeFile():
    decodedData = []
    decodedPass = ""
    openFileFrom = open(dataBase_Dest, "r")
    encryptedData = openFileFrom.read()
    openFileFrom.close()

    sortedData = base_64_b_fix(sortedData)

    for i in range(len(sortedData)):
        decodedPass = base64.b64decode(str(sortedData[i]))
        decodedData.append(decodedPass)
    for i in range(len(decodedData)):
        decodedData[i] = str(decodedData[i]).split("'")
    print('Saved passwords:')
    for lists in decodedData:
        print(lists[1])


def validateAdmin(checkedPass):
    openedPassFile = open(validationPass_Dest, "r")
    passFileData = openedPassFile.read()
    
    
    sortedPassData = base_64_b_fix(sortedPassData)
    
    actualPass = str(base64.b64decode(str(sortedPassData).encode("ascii")))
    actualPass = base_64_b_fix(actualPass)
    
    if actualPass[0] == str(checkedPass):
        return True
    else: 
        return False


def base_64_b_fix(list_to_clear):
    list_to_clear = list_to_clear.split("'")
    list_to_clear = list(filter(lambda a: a != 'b', list_to_clear))
    list_to_clear = list(filter(lambda a: a != '\nb', list_to_clear))
    list_to_clear = list(filter(lambda a: a != '\n', list_to_clear))
    cleanedList = list(filter(lambda a: a != '', list_to_clear))
    return cleanedList
    
    
def eraseDataFile():
    open(dataBase_Dest, "w").close()

if __name__ == '__main__':
    main()
    
"""
coded by:
         @@@  @@@@@@@   @@@@@@@ @@@  @@@ @@@@@@  @@@@@@@   
        @@@@  @@@@@@@@ @@@@@@@@ @@@  @@@ @@@@@@@ @@@@@@@@  
       @@!@!  @@!  @@@ !@@      @@!  @@@     @@@ @@!  @@@  
      !@!!@!  !@!  @!@ !@!      !@!  @!@     @!@ !@!  @!@  
     @!! @!!  @!@!!@!  !@!      @!@!@!@! @!@!!@  @!@!!@!   
    !!!  !@!  !!@!@!   !!!      !!!@!!!! !!@!@!  !!@!@!    
    :!!:!:!!: !!: :!!  :!!      !!:  !!!     !!: !!: :!!   
    !:::!!::: :!:  !:! :!:      :!:  !:!     :!: :!:  !:!  
         :::  ::   :::  ::: ::: ::   ::: :: :::: ::   :::  
         :::   :   : :  :: :: :  :   : :  : : :   :   : :

"""
