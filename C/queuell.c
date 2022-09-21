#include<stdio.h>
#include<stdlib.h>

struct Node{
	int data;
	struct Node *next;
};

struct Node *front=NULL,*rear=NULL;

/*struct Node* append(struct Node* front,struct Node* rear,int val){
	struct Node *new=(struct Node*)malloc(sizeof(struct Node));
	new->data=val;
	new->next=NULL;
	if(rear==NULL){
		front=new;
		return new;
	}
	rear->next=new;
	return new;
}

struct Node* pop(struct Node *front,struct Node *rear){
	if(front==NULL){
		printf("\nUnderflow\n\n");
		return front;
	}
	else{
		printf("\nPopped %d\n\n",front->data);
		struct Node *temp=front->next;
		free(front);
		if(temp==NULL)
			rear==NULL;
		return temp;
	}
}*/

void append(int val){
	struct Node *new=(struct Node*)malloc(sizeof(struct Node));
	new->data=val;
	new->next=NULL;
	if(rear==NULL){
		front=new;
		rear=new;
		return;
	}
	rear->next=new;
	rear=new;
}

void pop(){
	if(front==NULL){
		printf("\nUnderflow\n\n");
	}
	else{
		printf("\nPopped %d\n\n",front->data);
		struct Node *temp=front->next;
		free(front);
		if(temp==NULL)
			rear=NULL;
		front=temp;
	}
}

void display(struct Node *start){
	if(start==NULL)
		printf("\nEmpty Linked List\n\n");
	else{
		struct Node *ptr=start;
		while(ptr!=NULL){
			printf("%d ",ptr->data);
			ptr=ptr->next;
		}
		printf("\n\n");
	}
}

void main(){
	//struct Node *front=NULL,*rear=NULL;
	int ch=-1,inp;
	while(ch!=4){
		printf("\n1.Append\n2.Pop\n3.Display\n4.Exit\nEnter choice : ");
		scanf("%d",&ch);
		switch(ch){
			case 1:printf("Enter value : ");
				scanf("%d",&inp);
				//rear=append(front,rear,inp);
				append(inp);
				break;
			case 2://front=pop(front,rear);
				pop();
				break;
			case 3:display(front);break;
			case 4:break;
			default:printf("\nWrong input\n\n");
		}
	}
}
