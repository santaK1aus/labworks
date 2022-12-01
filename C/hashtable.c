#include<stdio.h>
#include<stdlib.h>
#define SIZE 50

struct item{
    char* key;
    char* value;
};
typedef struct item item;

struct table{
    item** items;//array of pointers to items
    int size;
    int count;
};
typedef struct table table;

unsigned long hashFunction(char* str){
    unsigned long c=0;
    for(int j=0;str[j];j++)
        c+=str[j];
    return c%SIZE;
}

item* createItem(char* key,char* value){
    item *newit=(item*)malloc(sizeof(item));
    newit->key=(char*)malloc(strlen(key)+1);
    newit->value=(char*)malloc(strlen(value)+1);

    strcpy(newit->key,key);
    strcpy(newit->value,value);
    return newit;
}

table* createTable(int size){
    table *newt=(table*)malloc(sizeof(table));
    newt->size=size;
    newt->count=0;
    newt->items=(item**)calloc(size,sizeof(item*));

    for(int i=0;i<size;i++)
        newt->items[i]=NULL;
    return newt;
}

void freeItem(item* it){
    free(it->key);
    free(it->value);
    free(it);
}

void freeTable(table* t){
    for(int i=0;i<t->size;i++){
        item* cur=t->items[i];
        if(cur!=NULL)
            freeItem(cur);
    }

    free(t->count);
    free(t->size);
    free(t->items);
    free(t);
}

int handleCollision(table* t,item* it){}

int insertItem(table* t,char* k,char* v){
    item* newit=createItem(k,v);
    int key=hashFunction(v);
    item* cur=t->items[key];
    
    if(cur==NULL){ //key doesnt exist
        if(t->count==t->size){
            //hash table is full
            printf("Hashtable is full: Insertion not possible\n");
            freeItem(newit);
            return 0;
        }
        t->items[key]=newit;
        t->count++;
        return 1;
    }
    else{ //Key is present
        if(strcmp(key,cur->key)==0){ //same key
            strcpy(t->items[key]->value,v);
            return 1;
        }
        else
            return handleCollision(t,newit); //handle collision
    }
}

