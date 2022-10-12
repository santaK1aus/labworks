#include<stdio.h>
#define MAX 50

char stk[MAX];
int pos=0;

char pop(){
	if(pos==0) return 'x';
	return stk[--pos];
}

void push(char ch){
	stk[pos++]=ch;
}

char peek(){
	if(pos==0) return 'x';
	return stk[pos-1];
}

int priority(char ch){
	switch(ch){
		case '^':return 4;
		case '%':return 3;
		case '*':
		case '/':return 2;
		case '+':
		case '-':return 1;
		case '(':return 0;
		case ')':return -1;
		default:;
	}
	return -2;
}

void main(){
	char exp[MAX];
	printf("Enter the expression : ");
	scanf("%s",exp);
	printf("\n");
	
	int i=0;
	while(exp[i]!='\0'){
		int pr=priority(exp[i]);
		if(pr==-2)
			printf("%c ",exp[i]);
		else if(pr==-1){
			while(priority(peek())>=1){
				printf("%c ",pop());
			}
			pop();
		}
		else{
			int prev=priority(peek());
			if(prev<pr||pr==0)
				push(exp[i]);
			else if(prev==pr){
				printf("%c ",pop());
				push(exp[i]);
			}
			else{
				while(priority(peek())>=pr)
					printf("%c ",pop());
				push(exp[i]);
			}
		}
		i++;
	}
	while(peek()!='x')
		printf("%c ",pop());
}
