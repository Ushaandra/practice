#include <stdio.h>
int main()
{
    int g;
    printf("Enter grade:");
    scanf("%d",&g);
    switch(g/10)
    {
        case 10:
        case 9:
        printf("A+");
        break;
        case 8:
        printf("A");
        break;
        case 7:
        printf("B");
        break;
        case 6:
        printf("C");
        break;
        case 5:
        printf("D");
        break;
        case 4:
        printf("E");
        break;
        default:
        printf("Fail");
        break;
    }
}