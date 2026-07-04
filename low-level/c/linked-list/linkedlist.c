#include <stdio.h>
#include <stdlib.h>
#include "linkedlist.h"

/**
 * @brief Adds element to list
 * @details Adds element to the front of list
 * @param list list
 * @param x element too be added to list
 */
int add(linkedlist *list, int x)
{
    // case: if list is empty or not empty
    node *new_node = malloc(sizeof(node));
    if (new_node == NULL)
    {
        return 0;
    }
    new_node->data = x;
    new_node->next = list->head;
    list->head = new_node;
    list->size++;
    return 1;
}

int size(linkedlist *list)
{
    return list->size;
}