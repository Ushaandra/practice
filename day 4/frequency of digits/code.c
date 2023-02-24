#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {


    int arr[10]={0,0,0,0,0,0,0,0,0,0},i=0,l;
    char s[1000];
    scanf("%s",&s);
    l=strlen(s);
    while(i<l)
    {
      switch(s[i])
      {
          case '0':
          arr[0]=arr[0]+1;
          break;
          case '1':
          arr[1]=arr[1]+1;
          break;
          case '2':
          arr[2]=arr[2]+1;
          break;
          case '3':
          arr[3]=arr[3]+1;
          break;
          case '4':
          arr[4]=arr[4]+1;
          break;
          case '5':
          arr[5]=arr[5]+1;
          break;
          case '6':
          arr[6]=arr[6]+1;
          break;
          case '7':
          arr[7]=arr[7]+1;
          break;
          case '8':
          arr[8]=arr[8]+1;
          break;
          case '9':
          arr[9]=arr[9]+1;
          break;
          
      }
      i++;
    }
    for(i=0;i<10;i++)
    printf("%d ",arr[i]);
    return 0;
    
    
}
