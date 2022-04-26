#include "lists.h"

/**
 * insert_node - Insert a node in a sorted linked list
 *
 * @head: Head of the list
 * @number: Value to add
 * Return: Address of the new node
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *current = (*head)->next, *old = *head;

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = number;

	if (number < (*head)->n)
	{
		new->next = *head;
		*head = new;
		return (new);
	}

	while (number > current->n)
	{
		current = current->next;
		old = old->next;
	}

	old->next = new;
	new->next = current;

	return (new);
}
