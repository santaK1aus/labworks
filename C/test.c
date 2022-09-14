#include<stdio.h>
#include<stdlib.h>

struct Node{
	int data;
	struct Node *next;
};

void main(){
	struct Node *t=(struct Node*)malloc(sizeof(struct Node));
	t->data=5;
	free(t);
	printf("done");
}
