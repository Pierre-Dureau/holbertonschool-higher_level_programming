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
	int length, i;
	int a, b;
	int *p = NULL, *t;

	if (*head == NULL)
		return (1);

	length = listint_len(*head);
	p = malloc(sizeof(length));
	t = p;

	for (i = 0; i < length; i++, t++)
	{
		*t = (*head)->n;
		*head = (*head)->next;
	}

	for (i = 0; i < length; i++, length--)
	{
		a = *(p + i);
		b = *(p + length - 1);

		if (a != b)
			return (0);
	}

	free(p);
	return (1);
}
