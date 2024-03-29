#include "lists.h"
#include <stdlib.h>
/**
 * insert_node - Inserts a number into a sorted singly-linked list.
 * @head: A pointer to the head of the linked list.
 * @number: The number to insert.
 *
 * Return: A pointer to the new node, or NULL on failure
*/
listint_t *insert_node(listint_t **head, int number)
{
listint_t *new_node, *current;
new_node = malloc(sizeof(listint_t));
if (!new_node)
return (NULL);
new_node->n = number;
if (*head == NULL || (*head)->n >= number)
{
new_node->next = *head;
*head = new_node;
return (new_node);
}
current = *head;
while (current->next && current->next->n < number)
current = current->next;
new_node->next = current->next;
current->next = new_node;
return (new_node);
}
