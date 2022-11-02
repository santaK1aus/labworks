#include<stdio.h>
#include<stdlib.h>
#define MAX 100

void swap(int *a,int *b){
	int t=*a;
	*a=*b;
	*b=t;
}

void maxheapify(int a[],int i,int n){
	int l=i*2,r=l+1,max=i;
	if(l<n & a[l]>a[max]) max=l;
	if(r<n & a[r]>a[max]) max=r;
	if(max!=i){
		swap(&a[i],&a[max]);
		maxheapify(a,max,n);
	}
}

void maxheap(int a[],int n){   //redundant function
	for(int i=n/2;i>=1;i--)
		maxheapify(a,i,n);
}

void heapSort(int a[],int n){
	maxheap(a,n);
	while(n>2){
		swap(&a[1],&a[n-1]);
		n--;
		maxheapify(a,1,n);
	}
}

void main(){
	int *a=(int*)malloc(MAX*sizeof(int));
	int ch,n=1;
	printf("Enter values (-1 to exit) : ");
	scanf("%d",&ch);
	while(ch!=-1){
		a[n++]=ch;
		printf("Enter : ");
		scanf("%d",&ch);
	}
	heapSort(a,n);
	printf("\nSorted array : \n");
	for(int i=1;i<n;i++)
		printf("%d ",a[i]);
}
