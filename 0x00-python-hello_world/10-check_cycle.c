#include "lists.h"
/**
 * check_cycle - check if the list have a cycle.
 * @list: the linked list.
 * Return: 0 if there is no cycle and 1 if there is a cycle.
 */
int check_cycle(listint_t *list)
{
	listint_t *a = list, *b = list;

	while (a && b && b->next)
	{
		a = a->next;
		b = b->next->next;
		if (a == b)
			return (1);
	}
	return (0);
}
  
