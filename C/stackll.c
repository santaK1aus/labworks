#include<stdio.h>
#include<stdlib.h>

struct Node{
	int data;
	struct Node *next;
};

struct Node* push(struct Node *start,int val){
	struct Node *new=(struct Node*)malloc(sizeof(struct Node));
	new->data=val;
	new->next=start;
	return new;
}

struct Node* pop(struct Node *start){
	if(start==NULL){
		printf("\nUnderflow\n\n");
		return start;
	}
	else{
		printf("\nPopped %d\n\n",start->data);
		struct Node *temp=start->next;
		free(start);
		return temp;
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
	struct Node *start=NULL;
	int ch=-1,inp;
	while(ch!=4){
		printf("\n1.PUSH\n2.POP\n3.Display\n4.Exit\nEnter choice : ");
		scanf("%d",&ch);
		switch(ch){
			case 1:printf("Enter value : ");
				scanf("%d",&inp);
				start=push(start,inp);
				break;
			case 2:start=pop(start);
				break;
			case 3:display(start);break;
			case 4:break;
			default:printf("\nWrong input\n\n");
		}
	}
}
