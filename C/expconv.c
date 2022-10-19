#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#define MAX 50

char stk[MAX];
float stki[MAX];
int pos=0,posi=0;

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

float popi(){
	if(posi==0) return -1;
	return stki[--posi];
}

void pushi(float ch){
	stki[posi++]=ch;
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

int s2int(char ch[]){
	int neg=(ch[0]=='-')?-1:1,i=(neg==-1)?1:0,res=0;
	while(ch[i]!='\0'){
		res=res*10+(int)ch[i++]-48;
	}
	return res*neg;
}

float s2float(char ch[]){
	int neg=(ch[0]=='-')?-1:1,i=(neg==-1)?1:0,res=0,end=0;
	float sub=0.0,fl=0.1;
	while(ch[i]!='.' && (end=(ch[i]!='\0')) )
		res=res*10+(int)ch[i++]-48;
	if(end==0) return neg*res;
	i++;
	while(ch[i]!='\0'){
		sub+=((int)ch[i++]-48)*fl;
		fl/=10;
	}
	//printf("%d %f\n",res,sub);
	return neg*(res+sub);
}

void evaluateVars(char exp[]){//Evaluate from variables
	float *vars=(float*)calloc(150,sizeof(float));
	int i=0;
	while(exp[i]!='\0'){
		int prio=priority(exp[i]);
		if(prio>0){
			float b=popi(),a=popi(),res;
			//printf("%f %f %c\n",a,b,exp[i]);
			switch(exp[i]){
				case '^':res=pow(a,b);break;
				case '%':res=(int)a%(int)b;break;
				case '*':res=a*b;break;
				case '/':res=a/b;break;
				case '+':res=a+b;break;
				case '-':res=a-b;break;
			}
			//printf("%f",res);
			pushi(res);
		}
		else{
			if(vars[exp[i]]==0){
				printf("Enter value for %c :",exp[i]);
				scanf("%f",&vars[exp[i]]);
			}
			//printf("%f\n",vars[exp[i]]);
			pushi(vars[exp[i]]);
			//printf("#deb %d",vars[exp[i]]);
		}
		i++;
	}
	printf("Final value : %f\n",popi());
}

void evaluateNums(char exp[]){//Evaluate from values directly
	int i=0,pos=0;
	char nums[MAX];
	while(exp[i]!='\0'){
		if(exp[i]==' '){
			if(priority(nums[pos-1])>0){
				float b=popi(),a=popi(),res;
				switch(nums[pos-1]){
					case '^':res=pow(a,b);break;
					case '%':res=(int)a%(int)b;break;
					case '*':res=a*b;break;
					case '/':res=a/b;break;
					case '+':res=a+b;break;
					case '-':res=a-b;break;
				}
				pushi(res);
				pos=0;
			}
			else{
				nums[pos]='\0';
				float d=s2float(nums);
				//printf("#val %f\n",d);
				pushi(d);
				pos=0;
			}
		}
		else
			nums[pos++]=exp[i];
		i++;
		//printf("#nums %s\n",nums);
	}
	printf("Final value : %f\n",popi());
}

void maina(){
	char exp[MAX],finexp[MAX];
	printf("Enter the expression : ");
	scanf("%s",exp);
	printf("\n");
	
	int i=0,x=0;
	while(exp[i]!='\0'){
		int pr=priority(exp[i]);
		if(pr==-2)
			printf("%c ",finexp[x++]=exp[i]);
		else if(pr==-1){
			while(priority(peek())>=1){
				printf("%c ",finexp[x++]=pop());
			}
			pop();
		}
		else{
			int prev=priority(peek());
			if(prev<pr||pr==0)
				push(exp[i]);
			else if(prev==pr){
				printf("%c ",finexp[x++]=pop());
				push(exp[i]);
			}
			else{
				while(priority(peek())>=pr)
					printf("%c ",finexp[x++]=pop());
				push(exp[i]);
			}
		}
		i++;
	}
	while(peek()!='x')
		printf("%c ",finexp[x++]=pop());
	finexp[x++]='\0';
	printf("\n");
	//evaluate(finexp);
	//printf("\n%s",finexp);
}

void main(){
	char exp[MAX];
	int ch;
	printf("Enter the expression : ");
	gets(exp);
	//printf("%f",s2float(exp));
	//evaluateNums(exp);
	evaluateVars(exp);
	/*printf("1. Evaluate using variables\n2. Evaluate directly\nEnter choice : ");
	scanf("%d\n",&ch);
	printf("\n");
	if(ch==1) evaluateNums(exp);
	else evaluateVars(exp);*/
}
