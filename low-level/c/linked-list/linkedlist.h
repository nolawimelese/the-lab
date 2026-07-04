#ifndef LINKEDLIST_H
#define LINKEDLIST_H

typedef struct node
{
    int data;
    struct node *next;
} node;

typedef struct linkedlist
{
    node *head;
    int size;
} linkedlist;

int add(linkedlist *list, int x);                // add element to end of list
int add_index(linkedlist *list, int x, int ind); // add element to index
int remove_index(linkedlist *list, int ind);     // remove element at index
int size(linkedlist *list);                      // return size of list
int set(linkedlist *list, int ind, int x);       // set value of element at index
int get(linkedlist *list, int ind);              // get value of element at index

#endif