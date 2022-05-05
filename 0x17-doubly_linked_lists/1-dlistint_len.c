#include "lists.h"
#include <stdio.h>
/**
 * dlistint_len -  number of nodes of a double linked list
 * @h: head
 * Return: the number of nodes
 */
size_t dlistint_len(const dlistint_t *h)
{
	size_t i = 0;

	while (h)
	{
		i++;
		h = h->next;
	}
	return (i);
}
