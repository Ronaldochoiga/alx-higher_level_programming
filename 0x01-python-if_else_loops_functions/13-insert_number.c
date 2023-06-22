#include "lists.h"

/**
 * insert_node - puts number in singly linked list
 * @head: pointer to the head of list
 * @number: inserting number
 *
 * Return: null or pointer to new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *nde = *head, *nw;

	nw = malloc(sizeof(listint_t));
	if (nw == NULL)
		return (NULL);
	nw->n = number;

	if (nde == NULL || nde->n >= number)
	{
		nw->next = nde;
		*head = nw;
		return (nw);
	}

	while (nde && nde->next && nde->next->n < number)
		nde = nde->next;

	nw->next = nde->next;
	nde->next = nw;

	return (nw);
}
