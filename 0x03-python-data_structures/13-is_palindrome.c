#include <stdio.h>
#include "lists.h"
/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: Double pointer to the head node.
 *
 * Return: 0 if not a palindrome, 1 if a palindrome.
 */
int is_palindrome(listint_t **head)
{
listint_t *slow, *fast, *prev, *temp;
slow = fast = *head;
prev = NULL;
if (*head == NULL || (*head)->next == NULL)
return (1);
while (fast && fast->next)
{
fast = fast->next->next;
temp = slow;
slow = slow->next;
temp->next = prev;
prev = temp;
}
if (fast)
slow = slow->next;
while (prev && slow)
{
if (prev->n != slow->n)
return (0);
prev = prev->next;
slow = slow->next;
}
return (1);
}
