#include<stdio.h>

void swap(int *a,int *b){
	int t=*a;
	*a=*b;
	*b=t;
}

void display(int a[],int n){
	for(int i=0;i<n;i++)
		printf("%d ",a[i]);
	printf("\n\n");
}

int partitionr(int a[],int p,int r){
	int piv=a[r];
	int i=p-1;
	for(int j=p;j<r;j++)
		if(a[j]<=piv)
			swap(&a[++i],&a[j]);
	swap(&a[++i],&a[r]);
	return i;
}

int partitionf(int a[],int p,int r){
	int piv=a[p];
	int i=r+1;
	for(int j=r;j>p;j--)
		if(a[j]>=piv)
			swap(&a[--i],&a[j]);
	swap(&a[--i],&a[p]);
	return i;
}

void quickSort(int a[],int p,int r){
	if(p<r){
		int q=partitionr(a,p,r);
		quickSort(a,p,q-1);
		quickSort(a,q+1,r);
	}
}

void quickSortf(int a[],int p,int r){
	if(p<r){
		int q=partitionf(a,p,r);
		quickSort(a,p,q-1);
		quickSort(a,q+1,r);
	}
}

void main(){
	//int a[]={5,8,9,7,4,2,2,1,0,4,7,89,-1},n=sizeof(a)/sizeof(int);
	int a[50],n=0,inp;
	printf("Enter values in array(-1 to exit) : ");
	scanf("%d",&inp);
	while(inp!=-1){
		a[n++]=inp;
		scanf("%d",&inp);
	}
	printf("Initial Array : ");
	display(a,n);
	printf("1.Use 1st value as pivot\n2.Use last value as pivot\nEnter choice : ");
	scanf("%d",&inp);
	(inp==1)?quickSortf(a,0,n-1):quickSort(a,0,n-1);
	display(a,n);
}
