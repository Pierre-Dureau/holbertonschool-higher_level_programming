#include "lists.h"

/**
 * check_cycle - Check if there is a loop in a linked list
 * @list: Head of the list
 * Return: 1 if there a loop, 0 if not
 */

int check_cycle(listint_t *list)
{
	listint_t *p1 = list, *p2 = list;

	if (!list)
		return (0);
	if (list == list->next)
		return (1);

	while (p1 && p1->next)
	{
		p1 = p1->next->next;
		p2 = p2->next;

		if (p1 == p2)
			return (1);
	}

	return (0);
}
