#include <stdio.h>
int main(){
    int i, j, max; 
    printf("Enter maximum value: ");
    scanf("%d", &max);
    for (i = 0, j = max; i <= max, j >= 0; i++, j--)
    {
        printf("%d  %d\n", i, j);
    }
    return 0;
}