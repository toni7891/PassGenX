# PassGenX - A program to generate passwords and keep them safe.

# Imported library's 
import random
import base64
import glob

# File destination addresses
dataBase_Dest = r"C:\Users\Tony\Desktop\passGen PROJECT\Encrypted_Data.txt"
validationPass_Dest = r"C:\Users\Tony\Desktop\passGen PROJECT\Admin.txt"
username_Dest = r"C:\Users\Tony\Desktop\passGen PROJECT\userList"
userPath = 'C:\\Users\\Tony\\Desktop\\passGen PROJECT\\userList\\'

def main():
    keepAlive = True
    user = userChoice()
    while keepAlive == True and user != False:
        keepAlive = menu(user)
        
    
def userChoice():
    userNameInput = input("""Welcome to PassGenX!
    please enter your username: """)
    allUsers = glob.glob(username_Dest + "/**/", recursive = True)
    sortedUserList = sortUsers(allUsers)

    for i in range(len(sortedUserList)):
        #check is username in DataBase:
        if str(sortedUserList[i]) == str(userPath + userNameInput + '\\'):
            #check User Pass:
            
            newPassPath = str(userPath + userNameInput + '\\pass.txt')
            userPass = input("    Please enter " + userNameInput + " Password: ")

            realPass = decryptUserPass(newPassPath)
            if userPass == realPass[0]:
                return userNameInput

            else:
                return False
       
     
def decryptUserPass(passPath):
    openPassFile = open(passPath, "r")
    unsortedUserPassData = openPassFile.read()
    openPassFile.close()
    sortedUserPassData = base_64_b_fix(unsortedUserPassData)

    actualUserPass = str(base64.b64decode(str(sortedUserPassData).encode("ascii")))
    actualUserPass = base_64_b_fix(actualUserPass)
    return actualUserPass
    
    
def menu(user):
    userChoiceMenu = """Welcome to PassGenX!
    please enter your username: """
    menuMassage = """
    Please select what operation do you want to execute:
    1- Create new Pass    
    2- See existing Passwords
    3- Erase Data file
    4- Change ADMIN Password
    5- Exit
    Your choice: """
    operationID = int(input(menuMassage))
    
    #todo -----> add multiuser functions to all operations!
    
    if operationID == 1:
        newPassLength = int(input("Please enter password length: "))
        NewpassGenerator(newPassLength)
        return True
    
    elif operationID == 2:
        validationID = input("Please enter Admin Password: ")
        if validateAdmin(validationID) == True:
            decryptDataBase()
        elif validateAdmin(validationID) == False:
            print('Wrong admin password...\nget the Fuck out!')
        return True
        
    elif operationID == 3:
        #add only active user DB erase!
        eraseDataFile()
        return True
        
    elif operationID == 4:
        #change to user change pass!
        validationID4 = input("Please enter Admin Password: ")
        if validateAdmin(validationID4) == True:
            isValid = True
            change_AdminPassword(isValid)
        elif validateAdmin(validationID4) == False:
            print('Wrong admin password...\nget the Fuck out!')
        return True
    

    elif operationID == 5:
        return False
        
    else: 
        print("There is no such Operation ID...")        

    

def NewpassGenerator(passLength):
    # possible symbol selection by absolute random 
    lowerLetterChars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u','v', 'w', 'x', 'y', 'z']
    upperLetterChars = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    specialChars = ['!', '@', '#', '$', '%', '&', '*']
    numberChars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    newPassWord = ""
    
    allChars = lowerLetterChars + upperLetterChars + numberChars + specialChars
    
    for i in range(passLength):
        newPassWord += random.choice(allChars)
    print('Your new password is: ' + newPassWord)
    inFile(encryptionAlgo(newPassWord), dataBase_Dest)
    print('your password have been encrypted!')
    print('Your Password has been saved!')
    
       
def encryptionAlgo(password):
    passBytes = password.encode('ascii')
    encodedPass = base64.b64encode(passBytes)

    return encodedPass

def inFile(encoded_Data, destToFile):
        fileOpen = open(destToFile, "a")
        fileOpen.write(str(encoded_Data) + '\n')
        fileOpen.close() 
 

def decryptDataBase():
    decodedData = []
    decodedPass = ""
    openFileFrom = open(dataBase_Dest, "r")
    encryptedData = openFileFrom.read()
    openFileFrom.close()

    sortedData = base_64_b_fix(encryptedData)

    for i in range(len(sortedData)):
        decodedPass = base64.b64decode(str(sortedData[i]))
        decodedData.append(decodedPass)
    for i in range(len(decodedData)):
        decodedData[i] = str(decodedData[i]).split("'")
    print('Saved passwords:')
    for lists in decodedData:
        print(lists[1])


def validateAdmin(validationPass): 
    openedPassFile = open(validationPass_Dest, "r")
    unsortedPassData = openedPassFile.read()
    openedPassFile.close()
    
    sortedPassData = base_64_b_fix(unsortedPassData)
    
    actualPass = str(base64.b64decode(str(sortedPassData).encode("ascii")))
    actualPass = base_64_b_fix(actualPass)
    
    if actualPass[0] == validationPass:
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

def sortUsers(fullUserList):
    sortedUsers = []

    for i in range(len(fullUserList)):
        if i == 0:
            i += 1
        else:
            sortedUsers.append(fullUserList[i])
    
    return sortedUsers
    
def eraseDataFile():
    open(dataBase_Dest, "w").close()
    print('Data Base file has been erased! ')

def change_AdminPassword(isValidated):
    if isValidated == True:
        newPass = input("Please enter a new Admin Password: ")
        encryptedPass = encryptionAlgo(newPass)
        dataFile = open(validationPass_Dest, 'w')
        dataFile.write(str(encryptedPass))
        print('Admin Password has been changed successfully! ')
        dataFile.close()

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
