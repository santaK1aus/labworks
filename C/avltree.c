#include<stdio.h>
#include<stdlib.h>

typedef struct Node Node;
struct Node{
    int val;
    int bal;
    Node *left;
    Node *right;
};

int height(Node *root){
    if(root==NULL)
        return 0;
    int lh=height(root->left),rh=height(root->right);
    return (lh>rh?lh:rh)+1;
}

Node* LLrot(Node *root){
    printf("LL rotated\n");
    Node *mov=root->left->right;
    root->left->right=root;
    root=root->left;
    root->right->left=mov;
    root->right->bal=height(root->right->left)-height(root->right->right);
    root->bal=height(root->left)-height(root->right);
    return root;
}

Node* LRrot(Node *root){
    printf("LR rotated\n");
    Node *mov=root->left->right;
    root->left->right=mov->left;
    mov->left=root->left;
    root->left=mov->right;
    mov->right=root;
    mov->left->bal=height(mov->left->left)-height(mov->left->right);
    mov->right->bal=height(mov->right->left)-height(mov->right->right);
    mov->bal=height(mov->left)-height(mov->right);
    return mov;
}

Node* RLrot(Node *root){
    printf("RL rotated\n");
    Node *mov=root->right->left;
    root->right->left=mov->right;
    mov->right=root->right;
    root->right=mov->left;
    mov->left=root;
    mov->left->bal=height(mov->left->left)-height(mov->left->right);
    mov->right->bal=height(mov->right->left)-height(mov->right->right);
    mov->bal=height(mov->left)-height(mov->right);
    return mov;
}

Node* RRrot(Node *root){
    printf("RR rotated\n");
    Node *mov=root->right->left;
    root->right->left=root;
    root=root->right;
    root->left->right=mov;
    root->left->bal=height(root->left->left)-height(root->left->right);
    root->bal=height(root->left)-height(root->right);
    return root;
}

Node* rebalance(Node *root){
    if(root->bal>1){
        if(root->left->bal==1)
            return LLrot(root);
        return LRrot(root);
    }
    else{
        if(root->right->bal==1)
            return RLrot(root);
        return RRrot(root);
    }
}

Node* insert(Node *root,int value){
    if(root==NULL){
        root=(Node*)malloc(sizeof(Node));
        root->val=value;
        root->left=root->right=NULL;
        root->bal=0;
        printf("Inserted %d\n",value);
    }
    else{
        if(value<root->val)
            root->left=insert(root->left,value);
        else
            root->right=insert(root->right,value);
        root->bal=height(root->left)-height(root->right);
        if(root->bal>1 || root->bal<-1){
            printf("Rebalancing at %d\n",root->val);
            root=rebalance(root);
            printf("Rebalanced root : %d\n",root->val);
        }
    }
    return root;
}

void display(Node *root){
    if(root==NULL) return;
    //printf("hi");
    display(root->left);
    display(root->right);
    printf("%d(%d)\t",root->val,root->bal);
}

void main(){
    Node *avl=NULL;
    avl=insert(avl,8);
    avl=insert(avl,12);
    avl=insert(avl,9);
    avl=insert(avl,11);
    avl=insert(avl,7);
    avl=insert(avl,6);
    avl=insert(avl,62);
    avl=insert(avl,15);
    avl=insert(avl,3);
    display(avl);
}