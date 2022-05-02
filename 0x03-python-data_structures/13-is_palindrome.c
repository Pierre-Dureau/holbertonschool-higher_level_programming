#include "lists.h"

/**
 * get_value - Get the value at index object
 *
 * @head: Head of the list
 * @index: Index of the node
 * Return: The value
 */

int get_value(listint_t *head, unsigned int index)
{
	unsigned int i = 0;
	listint_t *temp = head;

	while (i < index)
	{
		temp = temp->next;
		i++;
	}

	return (temp->n);
}

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

	if (*head == NULL)
		return (1);

	length = listint_len(*head) - 1;

	for (i = 0; i < length; i++, length--)
	{
		a = get_value(*head, i);
		b = get_value(*head, length);

		if (a != b)
			return (0);
	}
	return (1);
}
