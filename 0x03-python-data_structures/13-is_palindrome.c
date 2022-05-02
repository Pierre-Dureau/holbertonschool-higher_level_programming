#include "lists.h"

/**
 * listint_len - Count the number of elements in a listint_t list
 *
 * @h: Head of the list
 * Return: Number of elements
 */

int listint_len(listint_t *h)
{
	int count = 0;
	listint_t *temp = h;

	while (temp)
	{
		temp = temp->next;
		count++;
	}

	return (count);
}

/**
 * is_palindrome - Check if the linked list is a palindrome
 *
 * @head: Head of the list
 * Return: 1 if it's a palindrome, 0 if not
 */

int is_palindrome(listint_t **head)
{
	int length, i = 0, j = 0;
	int tab[100];
	listint_t *temp;

	if (*head == NULL)
		return (1);

	length = listint_len(*head);
	if (length == 1)
		return (1);

	temp = *head;

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
