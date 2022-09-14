#include<stdio.h>

int multiply(int a,int b){
	if(a==0||b==0)
		return 0;
	if(b<0)
		return -1*(a+multiply(a,b*-1-1));
	return a+multiply(a,b-1);
}

void main(){
	int a,b;
	printf("Enter 2 values : ");
	scanf("%d%d",&a,&b);
	printf("%d*%d = %d\n",a,b,multiply(a,b));
}
