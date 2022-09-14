#include<stdio.h>

int binSearchRec(int a[],int lb,int ub,int val){
	if(lb>ub)
		return -1;
	int mid=(lb+ub)/2;
	if(val>a[mid])
		return binSearch(a,mid+1,ub,val);
	else if(val<a[mid])
		return binSearch(a,lb,mid-1,val);
	else
		return mid;
}

int binSearch(int a[],int n,int val){
	int lb=0,ub=n-1,mid;
	while(lb<=ub){
		mid=(lb+ub)/2;
		if(val<a[mid])
			ub=mid-1;
		else if(val>a[mid])
			lb=mid+1;
		else
			return mid;
	}
	return -1;
}

void main(){
	
}
