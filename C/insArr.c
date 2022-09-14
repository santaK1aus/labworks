#include<stdio.h>
#define MAX 50

int a[MAX],n=0;

void parray(){
	if(n==0)
		printf("\nEmpty list\n\n");
	else{
		for(int i=0;i<n;i++)
			printf("%d ",a[i]);
		printf("\n\n");
	}
}

void insert(int ch,int pos){
	if(pos>n)
		pos=n;
	if(n>=50)
		printf("Overflow... Operation not possible");
	else{
		int i=n++;
		for(;i!=pos;i--)
			a[i]=a[i-1];
		a[i]=ch;
	}
}

void delete(int pos){
	if(pos>(n)||pos<0)
		printf("\nNot possible\n\n");
	else{
		int i=pos;
		for(;i<n;i++)
			a[i]=a[i+1];
		n--;
	}
}

void main(){
	int ch,pos;
	printf("Enter initial values in array(-1 to exit) : ");
	scanf("%d",&ch);
	while(ch!=-1){
		a[n++]=ch;
		printf("Enter : ");
		scanf("%d",&ch);
	}
	while(ch!=3){
		printf("\n1.Insertion\n2.Deletion\n3.Exit");
		printf("Enter choice : ");
		scanf("%d",&ch);
		switch(ch){
			case 1:printf("\nEnter value,position : ");
				scanf("%d%d",&ch,&pos);
				insert(ch,pos-1);
				parray();
				break;
			case 2:printf("Enter position : ");
				scanf("%d",&pos);
				delete(pos-1);
				parray();
				break;
			case 3:break;
			default:printf("\nWrong Input\n\n");
		}
	}
}
