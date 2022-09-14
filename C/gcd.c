#include<stdio.h>

int gcdr(int a,int b){
	if(a%b==0)
		return b;
	return gcdr(b,a%b);
}

void main(){
	int a,b;
	printf("Enter 2 values : ");
	scanf("%d%d",&a,&b);
	printf("GCD of %d and %d is %d\n",a,b,gcdr(a,b));
}
