#include <stdio.h>

/*
menu func
gen func
encryption func
write into file func
decrypt func
erase func
admin func
change admin pass
*/

#define MAX_LEN 20

void menu(void);
void newPassGen(int);

int main(void)
{
    menu();
    return 0;
}

void menu()
{
    int operationId = 0;
    int passLen = 0;

    printf("Welcome to PassGenX!\n    Please select what operation do you want to execute:\n1- Create new Pass\n2- See existing Passwords\n3- Erase Data file\n4- Change ADMIN Password\n5- Exit\nYour choice: ");
    scanf("%d", &operationId);
    if (operationId == 1)
    {
        printf("Please enter required Password length: ");
        scanf("%d", &passLen);
        newPassGen();
    }
    
}

void newPassGen(len)
{
    int passLengthReq = len;
    int newPassWord[MAX_LEN] = {}; 

}