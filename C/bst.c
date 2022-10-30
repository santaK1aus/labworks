#include<stdio.h>
#include<stdlib.h>

struct Node{
	int data;
	struct Node* left;
	struct Node* right;
};

struct Node* insert(struct Node* root, int val){
	if(root==NULL){
		struct Node* new=(struct Node*)malloc(sizeof(struct Node));
		new->data=val;
		new->left=NULL;
		new->right=NULL;
		return new;
	}
	if(val<root->data){
		root->left=insert(root->left,val);
	}
	else{
		root->right=insert(root->right,val);
	}
	return root;
}

int findLargest(struct Node* root){					//Expects initial root to be not NULL otherwise segfaults
	if(root->right!=NULL) return findLargest(root->right);
	else return root->data;
}

struct Node* delete(struct Node* root, int val){
	if(root==NULL) return NULL;
	if(root->data==val){
		if(root->left==NULL && root->right==NULL){
			free(root);
			return NULL;
		}
		if(root->left==NULL || root->right==NULL){
			struct Node* child=(root->left==NULL)?root->right:root->left;
			free(root);
			return child;
		}
		int max=findLargest(root->left);
		root->data=max;
		root->left=delete(root->left,max);
	}
	else if(val>root->data) root->right=delete(root->right,val);
	else root->left=delete(root->left,val);
	return root;
}

void inorder(struct Node* root){
	if(root==NULL) return;
	inorder(root->left);
	printf("%d ",root->data);
	inorder(root->right);
}

void preorder(struct Node* root){
	if(root==NULL) return;
	printf("%d ",root->data);
	preorder(root->left);
	preorder(root->right);
}

void postorder(struct Node* root){
	if(root==NULL) return;
	postorder(root->left);
	postorder(root->right);
	printf("%d ",root->data);
}

void main(){
	struct Node* start=NULL;
	int ch,val;
	do{
		printf("1.Insert\n2.Display In Order\n3.Display Pre Order\n4.Display Post Order\n5.Delete value\n6.Exit\nEnter choice : ");
		scanf("%d",&ch);
		switch(ch){
			case 1:printf("Enter value : ");
				scanf("%d",&val);
				start=insert(start,val);
				break;
			case 2:inorder(start);
				printf("\n\n");
				break;
			case 3:preorder(start);
				printf("\n\n");
				break;
			case 4:postorder(start);
				printf("\n\n");
				break;
			case 5:printf("Enter value : ");
				scanf("%d",&val);
				start=delete(start,val);
				break;
			case 6:break;
			default:printf("Wrong input\n");
		}
	}while(ch!=6);
}
