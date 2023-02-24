
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>


void calculate_the_maximum(int n, int k) {
  int i,j,a=0,r=0,x=0,a1=0,a2=0,r1=0,r2=0,x1=0,x2=0;
  for(i=1;i<n;i++)
  {
      for(j=i+1;j<=n;j++)
      {
        a1=i&j;
        if(a1<k && a1>=a2)
        a2=a1;
        r1=i|j;
        if(r1<k && r1>=r2)
        r2=r1;
        x1=i^j;
        if(x1<k && x1>=x2)
        x2=x1;
          
      }
  }
  printf("%d\n%d\n%d",a2,r2,x2);
}

int main() {
    int n, k;
  
    scanf("%d %d", &n, &k);
    calculate_the_maximum(n, k);
 
    return 0;
}
