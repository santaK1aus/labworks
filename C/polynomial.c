#include<stdio.h>
#include<stdlib.h>
#define MAX 50

typedef struct Node Node;

struct Node{
	int coff;
	int pow[3];
	struct Node *next;
};

struct Node* insert(struct Node *start,int c,int p[]){
	//Inserts new node according to the given coefficient and p int array which has the powers
	//Always inserts nodes at the end
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
	//Deletes node if start and del match, otherwise recurses
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
	//converts given char array to int with sign
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
	//compares if the given power arrays are equal, return 1 if so, otherwise 0
	for(int i=0;i<3;i++)
		if(a[i]!=b[i])
			return 0;
	return 1;
}

struct Node* strToExp(char e[]){
	//converts the given string to a linked list by extracting the numerals and chracters
	//requires '=' sign to denote eqn end (to fix later)
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
		}
	return start;
}

struct Node* add(struct Node* pa,struct Node* pb,int isSub){
	//Adds the 2nd linked list to the 1st
	//Empties the 2nd ll in the process
	//int isSub indicates if op is subtraction
	//Appends 2nd ll to 1st if any nodes/terms remain
	struct Node *tempa=pa, *tempi=pb,*del;
	int fl;
	while(tempi!=NULL){
		tempa=pa;
		fl=0;
		while(tempa!=NULL){
			if(compare(tempa->pow,tempi->pow)==1){
				tempa->coff+=tempi->coff*(isSub)?-1:1;
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
		tempi=pb;
		while(tempi!=NULL){
			tempi->coff*=(isSub)?-1:1;
			tempi=tempi->next;
		}
		tempa=pa;
		while(tempa->next!=NULL)
			tempa=tempa->next;
		tempa->next=pb;
	}
	pb=NULL;
	return pa;
}

Node* freeNode(Node *start){
	//deletes and frees the entire equation, if present
	while(start!=NULL)
		start=delete(start,start);
	return NULL;
}

void display(struct Node *start){
	struct Node *temp=start;
	char ch[]={'x','y','z'};
	while(temp!=NULL){
		int fl=(temp->coff<0);
		printf(" %c %d",(fl)?'-':'+',(fl)?temp->coff*-1:temp->coff);
		for(int i=0;i<3;i++){
			if(temp->pow[i]==1)
				printf("%c",ch[i]);
			else if(temp->pow[i]!=0)
				printf("%c^%d",ch[i],temp->pow[i]);
		}
		temp=temp->next;
		//printf("  ");
	}
	if(start!=NULL)
		printf(" = 0");
	else
		printf("Empty equation");
	printf("\n\n");
}

Node* compress(Node* start){
	//adds up terms with similar powers within the same equation
	//Eg. 2x+3y+5x=0 --> 7x+3y=0
	if(start==NULL) return start;
	Node *temp=start->next,*cur,*del;
	int fl;
	while(temp!=NULL){
		cur=start;
		fl=0;
		while(cur!=temp){
			if(compare(temp->pow,cur->pow)==1){
				cur->coff+=temp->coff;
				del=temp;
				fl++;
				break;
			}
			cur=cur->next;
		}
		temp=temp->next;
		if(fl>0)
			start=delete(start,del);
	}
	return start;
}

int count(Node *start){
	//Counts the number of terms in the equation
	int c=0;
	Node *t=start;
	while(t!=NULL){
		t=t->next;
		c++;
	}
	return c;
}

Node* mult(Node *p1,Node *p2){
	//if p2 has n nodes, n-1 copies of p1 are appended to itself
	//then the nodes of p2 are multiplied to nodes of p1
	//p2 is emptied at the end
	int p;
	if((p=p1==NULL) || p2==NULL){
		printf("Invalid Operation... Original equation retained\n");
		return (p==1)?p2:p1;
	}
	Node *t1=p1,*t2=p2;
	int c2=count(p2),c1=count(p1),tmp1=c1,tmp2=c2-1;
	while(tmp2--){
		tmp1=c1;
		while(tmp1--){
			p1=insert(p1,t1->coff,t1->pow);
			t1=t1->next;
		}
	}
	t1=p1;
	while(t2!=NULL){
		tmp1=c1;
		while(tmp1--){
			t1->coff*=t2->coff;
			t1->pow[0]+=t2->pow[0];
			t1->pow[1]+=t2->pow[1];
			t1->pow[2]+=t2->pow[2];
			t1=t1->next;
		}
		t2=t2->next;
	}
	p2=freeNode(p2);
	p1=compress(p1);
	return p1;
}

void main(){
	struct Node *polya=NULL, *polyb=NULL;
	char a[MAX];
	printf("Enter 1st Polynomial : ");
	gets(a);
	polya=strToExp(a);
	printf("Polynomial A : ");
	polya=compress(polya);
	display(polya);
	printf("Enter 2nd Polynomial : ");
	gets(a);
	polyb=strToExp(a);
	polyb=compress(polyb);
	printf("Polynomial B : ");
	display(polyb);
	printf("1.Sum\n2.Product\nEnter : ");
	int ch;
	scanf("%d",&ch);
	polya=(ch==2)?mult(polya,polyb):add(polya,polyb,0);
	printf("%s : ",(ch==2)?"Product":"Sum");
	display(polya);
	//display(polyb);
}