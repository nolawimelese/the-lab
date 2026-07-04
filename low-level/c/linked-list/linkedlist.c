#include <stdio.h>
#include <stdlib.h>
#include "linkedlist.h"

/**
 * @brief Adds element to front of list
 * @param list list
 * @param x element to be added to list
 * @return 0 if add was successful, -1 otherwise
 */
int add(linkedlist *list, int x)
{
    // invalid args
    if (list == NULL)
    {
        return -1;
    }
    node *new_node = malloc(sizeof(node));
    if (new_node == NULL)
    {
        return -1;
    }
    new_node->data = x;
    new_node->next = list->head;
    list->head = new_node;
    list->size++;
    return 0;
}

/**
 * @brief Adds element to specified index
 * @param list list
 * @param ind index at which to insert the element (0 to size, inclusive)
 * @param x element to be added to list
 * @return 0 if add was successful, -1 otherwise
 */
int add_index(linkedlist *list, int ind, int x)
{
    // invalid args (ind == size is valid: appends to end)
    if (list == NULL || ind < 0 || ind > list->size)
    {
        return -1;
    }
    node *curr = list->head;
    int i = 0;
    // case 1: index is first element
    if (ind == 0)
    {
        return add(list, x);
    }
    // case 2: index is in middle of list
    while (i < ind - 1 && curr != NULL)
    {
        curr = curr->next;
        i++;
    }
    node *new_node = malloc(sizeof(node));
    if (new_node == NULL)
    {
        return -1;
    }
    new_node->data = x;
    new_node->next = curr->next;
    curr->next = new_node;
    list->size++;
    return 0;
}

/**
 * @brief Removes element at specified index
 * @param list list
 * @param ind index of node to remove
 * @return removed element's value if successful, -1 otherwise
 */
int remove_index(linkedlist *list, int ind)
{
    // invalid args
    if (list == NULL || ind < 0 || ind > list->size - 1)
    {
        return -1;
    }
    // case 1: index is first element
    if (ind == 0)
    {
        node *old_head = list->head;
        int removed = old_head->data;
        list->head = old_head->next;
        free(old_head);
        list->size--;
        return removed;
    }
    // case 2: index is in the middle
    node *curr = list->head;
    int i = 0;
    while (i < ind - 1 && curr != NULL)
    {
        curr = curr->next;
        i++;
    }
    node *old_elem = curr->next;
    int removed = old_elem->data;
    curr->next = old_elem->next;
    free(old_elem);
    list->size--;
    return removed;
}

/**
 * @brief Returns size of list
 * @param list list
 * @return size of list
 */
int size(linkedlist *list)
{
    // invalid args
    if (list == NULL)
    {
        return -1;
    }
    return list->size;
}

/**
 * @brief Sets element of node in list at index to new element
 * @param list list
 * @param ind index of node
 * @param x new element
 * @return 0 if set was successful, -1 otherwise
 */
int set(linkedlist *list, int ind, int x)
{
    // invalid args
    if (list == NULL || ind < 0 || ind > list->size - 1)
    {
        return -1;
    }
    node *curr = list->head;
    int i = 0;
    while (i < ind && curr != NULL)
    {
        curr = curr->next;
        i++;
    }
    if (curr == NULL)
    {
        return -1;
    }
    curr->data = x;
    return 0;
}

/**
 * @brief Gets element of node in list at index
 * @param list list
 * @param ind index of node
 * @return Element at index if successful, -1 otherwise
 */
int get(linkedlist *list, int ind)
{
    // invalid args
    if (list == NULL || ind < 0 || ind > list->size - 1)
    {
        return -1;
    }
    node *curr = list->head;
    int i = 0;
    while (i < ind && curr != NULL)
    {
        curr = curr->next;
        i++;
    }
    if (curr == NULL)
    {
        return -1;
    }
    return curr->data;
}
