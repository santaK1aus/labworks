#include<stdio.h>
#include<stdlib.h>
#define MAX 50

struct Node{
	int coff;
	//char vars={'x','y','z'};
	int pow[3];
	struct Node *next;
};

struct Node* insert(struct Node *start,int c,int p[]){
	struct Node *new=(struct Node*)malloc(sizeof(struct Node)),*temp=start;
	new->coff=c;
	for(int i=0;i<3;i++)
		new->pow[i]=p[i];
	new->next=NULL;
	if(temp==NULL)
		start=new;
	else{
		while(temp->next!=NULL)
			temp=temp->next;
		temp->next=new;
	}
	return start;
}

struct Node* delete(struct Node *start,struct Node *del){
	if(start==del){
		struct Node *temp=del->next;
		free(del);
		return temp;
	}
	else
		start->next=delete(start->next,del);
	return start;
}

int s2int(char ch[]){
	if(ch[0]=='\0') return 1;
	else if(ch[0]=='-'  && ch[1]=='\0') return -1;
	int neg=(ch[0]=='-')?-1:1,i=(neg==-1)?1:0,res=0;
	while(ch[i]!='\0'){
		res=res*10+(int)ch[i++]-48;
	}
	return res*neg;
}

void join(){}

int compare(int a[],int b[]){
	for(int i=0;i<3;i++)
		if(a[i]!=b[i])
			return 0;
	return 1;
}

struct Node* strToExp(char e[]){
	struct Node *start=NULL;
	int i=0,coff=0,p[3]={0,0,0},ch=-1,x=0;
	char conv[MAX];
	conv[0]='\0';
	while(e[i]!='\0'){
		if(((e[i]=='+' || e[i]=='-') && i!=0) || e[i]=='='){
			conv[x++]='\0';
			if(ch==-1)
				coff=s2int(conv);
			else
				p[ch]=s2int(conv);
			start=insert(start,coff,p);
			coff=0;
			ch=-1;
			x=0;
			p[0]=p[1]=p[2]=0;
			if(e[i]=='-'){
				conv[x++]='-';
			}
			if(e[i]=='=') break;
		}
		else if(e[i]=='x' || e[i]=='y' || e[i]=='z'){
			conv[x++]='\0';
			if(ch==-1)
				coff=s2int(conv);
			else
				p[ch]=s2int(conv);
			x=0;
			conv[0]='\0';
			ch=(e[i]=='x')?0:(e[i]=='y')?1:2;
		}
		else conv[x++]=e[i];
		i++;
		//printf("%s\t%c\n",conv,e[i]);
	}
	return start;
}

struct Node* add(struct Node* pa,struct Node* pb){
	struct Node *tempa=pa, *tempi=pb,*del;
	int fl;
	while(tempi!=NULL){
		tempa=pa;
		fl=0;
		while(tempa!=NULL){
			if(compare(tempa->pow,tempi->pow)==1){
				tempa->coff+=tempi->coff;
				del=tempi;
				tempi=tempi->next;
				pb=delete(pb,del);
				fl++;
				break;
			}
			tempa=tempa->next;
		}
		if(fl==0)
			tempi=tempi->next;
	}
	if(pb!=NULL){
		tempa=pa;
		while(tempa->next!=NULL)
			tempa=tempa->next;
		tempa->next=pb;
	}
}

void display(struct Node *start){
	struct Node *temp=start;
	char ch[]={'x','y','z'};
	while(temp!=NULL){
		if(temp->coff>0 && temp!=start)
			printf("+");
		printf("%d",temp->coff);
		for(int i=0;i<3;i++){
			if(temp->pow[i]==1)
				printf("%c",ch[i]);
			else if(temp->pow[i]!=0)
				printf("%c^%d",ch[i],temp->pow[i]);
		}
		temp=temp->next;
		printf("  ");
	}
	printf("\n\n");
}

void main(){
	struct Node *polya=NULL, *polyb=NULL;
	char a[MAX];
	printf("Enter 1st Polynomial : ");
	gets(a);
	polya=strToExp(a);
	printf("Polynomial A : ");
	display(polya);
	printf("Enter 2nd Polynomial : ");
	gets(a);
	polyb=strToExp(a);
	printf("Polynomial B : ");
	display(polyb);
	polya=add(polya,polyb);
	printf("Sum : ");
	display(polya);
}
