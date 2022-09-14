#include<stdio.h>
#include<stdlib.h>

struct Node{
	int data;
	struct Node* next;
};

struct Node* append(struct Node* start,int val){//Add node at end
	struct Node* new=(struct Node*)malloc(sizeof(struct Node)),*ptr=start;
	if(new==NULL){
		printf("Oveflow");
		return start;
	}
	new->data=val;
	new->next=NULL;
	if(start==NULL)
		start=new;
	else{
		while(ptr->next!=NULL)
			ptr=ptr->next;
		ptr->next=new;
	}
	return start;
}

struct Node* appendf(struct Node* start,int val){//Add node at beginning
	struct Node* new=(struct Node*)malloc(sizeof(struct Node));
	if(new==NULL){
		printf("Oveflow");
		return start;
	}
	new->data=val;
	new->next=start;
	return new;
}

int count(struct Node *start){//Count Nodes
	int c=0;
	struct Node *ptr=start;
	while(ptr!=NULL){
		ptr=ptr->next;
		c++;
	}
	return c;
}

struct Node* insert(struct Node* start,int val,int pos){//Insert new Node at pos
	if(pos<=0)
		return appendf(start,val);
	struct Node* new=(struct Node*)malloc(sizeof(struct Node)),*ptr=start;
	int c=1;
	if(new==NULL){
		printf("Oveflow");
		return start;
	}
	new->data=val;
	while(c!=pos && ptr->next!=NULL){
		c++;
		ptr=ptr->next;
	}
	new->next=ptr->next;
	ptr->next=new;
	return start;
}

void display(struct Node *start){
	printf("\n");
	if(start==NULL){
		printf("Empty List\n\n");
		return;
	}
	struct Node *ptr=start;
	while(ptr!=NULL){
		printf("%d ",ptr->data);
		ptr=ptr->next;
	}
	printf("\n\n");
}

void main(){
	struct Node* start=NULL;
	int ch=-1,inp,pos;
	while(ch!=6){
		printf("1.Add node at front\n2.Add node at rear\n3.Add node at pos\n4.Display number of nodes\n5.Display List\n6.Exit\nEnter choice : ");
		scanf("%d",&ch);
		switch(ch){
			case 1:printf("Enter value : ");
				scanf("%d",&inp);
				start=appendf(start,inp);
				break;
			case 2:printf("Enter value : ");
				scanf("%d",&inp);
				start=append(start,inp);
				break;
			case 3:printf("Enter value, position : ");
				scanf("%d%d",&inp,&pos);
				start=insert(start,inp,pos);
				break;
			case 4:printf("\n%d nodes present\n\n",count(start));
				break;
			case 5:display(start);break;
			case 6:break;
			default:printf("\nWrong input\n\n");
		}
	}
}
