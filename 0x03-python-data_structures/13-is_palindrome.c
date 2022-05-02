#include "lists.h"

/**
 * is_palindrome - Check if the linked list is a palindrome
 *
 * @head: Head of the list
 * Return: 1 if it's a palindrome, 0 if not
 */

int is_palindrome(listint_t **head)
{
	int length = 0, i = 0;
	int tab[100];
	listint_t *temp;

	if (*head == NULL)
		return (1);

	temp = *head;
	while (temp != NULL)
	{
		tab[length] = temp->n;
		temp = temp->next;
		length++;
	}
	if (length < 2)
		return (1);

	length--;
	while (i < length)
	{
		if (tab[i] != tab[length])
			return (0);
		length--;
		i++;
	}

	return (1);
}
