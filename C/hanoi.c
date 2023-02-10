#include<stdio.h>
#include<math.h>

void toh(int n,char from, char to, char aux){
    if(n==1){
        printf("Move 1 from %c to %c\n",from,to);
        return;
    }
    toh(n-1,from, aux, to);
    printf("Move %d from %c to %c\n",n,from,to);
    toh(n-1,aux, to, from);
}

void main(){
    char f='A',a='B',t='C';
    int n;
    printf("Enter number of rings : ");
    scanf("%d",&n);
    toh(n,f,a,t);
}