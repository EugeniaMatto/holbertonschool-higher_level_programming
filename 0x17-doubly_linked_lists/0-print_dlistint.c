#include "lists.h"
#include <stdio.h>
/**
 * print_dlistint - prints all the elements of a dlistint_t list.
 * @h: head
 * Return: the number of nodes
 */
size_t print_dlistint(const dlistint_t *h)
{
	int i = 0;

	if (h)
	{
		while (h->next)
		{
			printf("%d\n", h->n);
			i++;
			h = h->next;
		}
		printf("%d\n", h->n);
		i++;
	}
	return (i);
}
