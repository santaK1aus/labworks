#include<stdio.h>
#include<stdlib.h>

struct Node{
	int data;
	struct Node *next;
};

struct Node * create(struct Node *start){
	struct Node *new,*ptr=start;
	int ch;
	printf("%d",ch);
	if(start!=NULL){
		while(ptr->next!=start)
			ptr=ptr->next;
	}
	printf("\nEnter value (-1 to exit) :");
	scanf("%d",&ch);
	while(ch!=-1){
		new=(struct Node *)malloc(sizeof(struct Node));
		new->data=ch;
		if(ptr==NULL){
			start=new;
			start->next=start;
			ptr=start;
		}
		else{
			new->next=start;
			ptr->next=new;
			ptr=new;
		}
		printf("Enter value : ");
		scanf("%d",&ch);
	}
	printf("\n\n");
	return start;
}

struct Node * insert(struct Node *start,int val,int pos){
	struct Node *new=(struct Node*)malloc(sizeof(struct Node)),*ptr=start;
	new->data=val;
	if(start==NULL){
		new->next=new;
		return new;
	}
	while(ptr->next!=start)
		ptr=ptr->next;
	if(pos==0){
		new->next=start;
		ptr->next=new;
		return new;
	}
	else if(pos==-1){
		ptr->next=new;
		new->next=start;
	}
	else{
		int c=1;
		ptr=start;
		while(c!=pos && ptr->next!=start){
			c++;
			ptr=ptr->next;
		}
		new->next=ptr->next;
		ptr->next=new;
	}
	return start;
}

struct Node * delete(struct Node *start,int val,int pos){
	struct Node *ptr,*preptr;
	if(start==NULL){
		printf("\nUnderflow\n\n");
		return start;
	}
	else if(start->next==start && (val==-1 || start->data==val)){
		free(start);
		return NULL;
	}
	else if(pos==0){
		preptr=start;
		ptr=start;
		while(ptr->next!=start)
			ptr=ptr->next;
		start=start->next;
		ptr->next=start;
		free(preptr);
	}
	else if(pos==-1){
		preptr=start;
		ptr=start;
		while(ptr->next!=start){
			preptr=ptr;
			ptr=ptr->next;
		}
		preptr->next=start;
		free(ptr);
	}
	else if(pos==-2){//NUKE THE ENTIRE LIST
		ptr=start->next;
		while(ptr->next!=start){
			preptr=ptr;
			ptr=ptr->next;
			free(preptr);
		}
		free(ptr);
		free(start);
		printf("\nENTIRE LIST DELETED\n\n");
		return NULL;
	}
	else{
		int fl=0;
		ptr=start;
		while(ptr->next!=start)
			ptr=ptr->next;
		preptr=ptr;
		ptr=start;
		while(fl=(ptr->next!=start)){
			if(ptr->data==val){
				preptr->next=ptr->next;
				if(ptr==start)
					start=start->next;
				free(ptr);
				break;
			}
			preptr=ptr;
			ptr=ptr->next;
		}
		if(fl==0)
			printf("\nNOT FOUND\n\n");
	}
	return start;
}

void display(struct Node *start){
	if(start==NULL)
		printf("\nEmpty List\n\n");
	else{
		struct Node *ptr=start;
		while(ptr->next!=start){
			printf("%d ",ptr->data);
			ptr=ptr->next;
		}
		printf("%d \n\n",ptr->data);
	}
}

void main(){
	int ch=-1,inp,pos;
	struct Node *start=NULL;
	
	while(ch!=11){
		printf("1.Create List\t\t\t2.Insert at Beggining\n3.Insert at End\t\t\t4.Insert after position\n5.Insert before position\t6.Delete at End\n7.Delete at beginning\t\t8.Delete entire List\n9.Delete item\t\t\t10.Display\n11.Exit\nEnter Choice : ");
		scanf("%d",&ch);
		if((ch>=2 && ch<=5) || ch==9){
			printf("\nEnter value : ");
			scanf("%d",&inp);
		}
		if(ch==4 || ch==5){
			printf("Enter Position : ");
			scanf("%d",&pos);
		}
		switch(ch){
			case 1:start=create(start);break;
			case 2:start=insert(start,inp,0);break;
			case 3:start=insert(start,inp,-1);break;
			case 4:start=insert(start,inp,pos);break;
			case 5:start=insert(start,inp,pos-1);break;
			case 6:start=delete(start,-1,-1);break;
			case 7:start=delete(start,-1,0);break;
			case 8:start=delete(start,-1,-2);break;
			case 9:start=delete(start,inp,1);break;
			case 10:display(start);break;
			case 11:break;
			default:printf("\nWrong Input\n\n");
		}
	}
}
