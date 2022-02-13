import base64

# Global variables
dataBase_Dest = r"C:\Users\Tony\Desktop\passGen PROJECT\Encrypted_Data.txt"
validationPass_Dest = r"C:\Users\Tony\Desktop\passGen PROJECT\Admin.txt"

def validateAdmin(validationPass):
    openedPassFile = open(validationPass_Dest, "r")
    unsortedPassData = openedPassFile.read()
    print(unsortedPassData)
    sortedPassData = base_64_b_fix(unsortedPassData)
    print(sortedPassData)
    actualPass = str(base64.b64decode(str(sortedPassData).encode("ascii")))
    print(actualPass)
    actualPass = base_64_b_fix(actualPass)
    print(actualPass)
    print(validationPass)
    if str(actualPass[0]) == str(validationPass):
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

ggPass = "adminPass"
if validateAdmin(ggPass) == True:
    print("goodddd")
elif validateAdmin(ggPass) == False:
    print("nahhhhhhh")
