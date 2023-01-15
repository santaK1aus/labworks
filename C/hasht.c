#include<stdio.h>
#include<math.h>
#include<stdlib.h>

int hashDiv(int k,int size){
	return k%size;
}

int hashMult(int k, int size){
	float a = (pow(5,0.5)-1)/2;
	a = k*a;//-((int)k*a);
	a-=(int)a;
	printf("in mult : %f\n",a);
	return (int)(a*size);
}

int hashMidSq(int k, int size){
	int ks=0,ss=0,k2=k*k,t=k2;
	while(t>0){
		t/=10;
		ks+=1;
	}
	t=size-1;
	ks/=2;
	while(t>0){
		t/=10;
		ss+=1;
	}
	int f=(int)pow(10,ks+ss-1),r=(int)pow(10,ks-ss/2);
	return ((k2%f)/r)%size;
}

int hashFold(int k, int size){
	int ss=0,ks=0,t=size-1,rem=0,sum=0;
	while(t>0){
		t/=10;
		ss++;
	}
	t=k;
	while(t>0){
		t/=10;
		ks++;
	}
	t=ks/ss;
	rem=ks%ss;
	ss=(int)pow(10,ss);
	sum+=k%(int)pow(10,rem);
	k/=(int)pow(10,rem);
	while(t>0){

		sum+=k%ss;
		k/=ss;
		t--;
	}
	return (sum%ss)%size;
}

void displayTable(int *arr,int size){
	int i=0;
	while(i<size)
		printf("table[%d] --> %d\n",i,arr[i++]);
	printf("\n");
}

void main(){
	int size, key, ch;
	printf("Enter size of hash table : ");
	scanf("%d",&size);
	int *arr=(int*)malloc(size*sizeof(int));
	for(int i=0;i<size;i++)
		arr[i]=-1;
	do{	
		printf("Enter key (-1 to exit, -2 to display table): ");
		scanf("%d",&key);
		switch(key){
			case -1:exit(0);break;
			case -2:displayTable(arr,size);continue;
			//case -3:fetchKey(arr,size,key);
			default:if(key<0){
						printf("\nWrong Input\n");
						continue;
						}
		}
		printf("1. Division\n2. Multiplication\n3. Mid-Square\n4. Folding Method\nEnter Choice : ");
		scanf("%d",&ch);
		int index,t;
		switch(ch){
			case 1:index=hashDiv(key,size);break;
			case 2:index=hashMult(key,size);break;
			case 3:index=hashMidSq(key,size);break;
			case 4:index=hashFold(key,size);break;
			default:printf("Wrong choice\n");
			continue;
		}
		t=index;
		do{
			if(arr[index]==-1){
				arr[index]=key;
				printf("Key %d placed at index %d\n",key,index);
				t=-1;
				break;
			}
			index=(index+1)%size;
		}while(t!=index);
		if(t==index)
			printf("Overflow\n");
	}while(ch!=-1);
}
