#include<stdio.h>
#include<stdlib.h>

struct Node{
	int data;
	struct Node *next;
};

int s2int(char ch[]){
	int neg=(ch[0]=='-')?-1:1,i=(neg==-1)?1:0,res=0;
	while(ch[i]!='\0'){
		res=res*10+(int)ch[i++]-48;
	}
	return res*neg;
}

void main(){
	char ch[]="-1469";
	int d=s2int(ch);
	printf("%d",d);
}


