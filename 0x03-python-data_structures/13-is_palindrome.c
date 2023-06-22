#include "lists.h"

listint_t *reverse_listint(listint_t **head);
int is_palindrome(listint_t **head);

/**
 * reverse_listint - converts singly linked lst
 * @head: pointer to head in reverse
 *
 * Return: pointer to head of reverse linked list
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *nde = *head, *next, *previous = NULL;

	while (nde)
	{
		next = nde->next;
		nde->next = previous;
		previous = nde;
		nde = next;
	}

	*head = previous;
	return (*head);
}

/**
 * is_palindrome - checks if palindrome
 * @head: pointer to the head of the linked lists
 *
 * Return: 0 or -1
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp, *rev, *middle;
	size_t sis = 0, i;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	temp = *head;
	while (temp)
	{
		sis++;
		temp = temp->next;
	}

	temp = *head;
	for (i = 0; i < (sis / 2) - 1; i++)
		temp = temp->next;

	if ((sis % 2) == 0 && temp->n != temp->next->n)
		return (0);

	temp = temp->next->next;
	rev = reverse_listint(&temp);
	middle = rev;

	temp = *head;
	while (rev)
	{
		if (temp->n != rev->n)
			return (0);
		temp = temp->next;
		rev = rev->next;
	}
	reverse_listint(&middle);

	return (1);
}
