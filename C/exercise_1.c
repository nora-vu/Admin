#include <stdio.h>
int main(){
    
    //Khai bao bien:
    int a;
    int b;
    int min;
    int max;
    int i;
    
    //Nhap bien:
    start:
    printf("Enter number a: ");
    scanf("%d", &a);
    printf("Enter number b: ");
    scanf("%d", &b);
    
    //So sanh hon kem:
    if (a > b) {
        max = a;
        min = b;
    }
    else if (a < b) {
        min = a;
        max = b;
    }
    else {
        printf("Please enter unequal numbers.");
        goto start;
    }

    //Vong lap:
    for (i = min; i <= max; i++) {
        if (i % 2 == 0){
            printf("%d\n", i);      
        }
    }
    return 0;
}