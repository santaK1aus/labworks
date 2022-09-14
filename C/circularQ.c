#include<stdio.h>
#define MAX 5

int a[MAX],head=-1,tail=-1;

void insert(){
	if((head-1)==tail || (head==0 && tail==(MAX-1)))
		printf("\nOverflow\n");
	else{
		printf("\nEnter value : ");
		tail=(tail+1)%MAX;
		scanf("%d",&a[tail]);
		if(head==-1)
			head=0;
	}
	printf("\n");
}

void delete(){
	if(head==-1)
		printf("\nUnderflow\n\n");
	else{
		printf("\nValue at front deleted\n\n");
		if(head==tail){
			head=-1;
			tail=-1;
		}
		else
			head=(head+1)%MAX;
	}
}

void display(){
	if(head==-1)
		printf("\nEmpty List\n\n");
	else{
		printf("\n");
		int i=head-1;
		do{
			i=(i+1)%MAX;
			printf("%d ",a[i]);
		}while(i!=tail);
		printf("\n\n");
	}
}

void main(){
	int ch=-1;
	while(ch!=4){
		printf("1.Insert\n2.Delete\n3.Display Queue\n4.Exit\nEnter Choice : ");
		scanf("%d",&ch);
		switch(ch){
			case 1:insert();
				break;
			case 2:delete();
				break;
			case 3:display();
				break;
			case 4:break;
			default: printf("\nWrong Input\n\n");
		}
	}
}
