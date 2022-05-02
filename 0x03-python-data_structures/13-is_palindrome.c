#include "lists.h"

/**
 * is_palindrome - Check if the linked list is a palindrome
 *
 * @head: Head of the list
 * Return: 1 if it's a palindrome, 0 if not
 */

int is_palindrome(listint_t **head)
{
	int length = 0, i = 0, j = 0;
	int tab[100];
	listint_t *temp = *head;

	temp = *head;
	while (temp)
	{
		temp = temp->next;
		length++;
	}
	if (length < 2)
		return (1);

	while (temp != NULL)
	{
		tab[i] = temp->n;
		temp = temp->next;
		i++;
	}

	i--;
	length--;
	while (i >= (length / 2))
	{
		if (tab[j] != tab[i])
			return (0);
		j++;
		i--;
	}

	return (1);
}
