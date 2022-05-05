#include "lists.h"
#include <stdio.h>
/**
 * get_dnodeint_at_index -  returns the index node
 * @head: head
 * @index: index
 * Return: index node adress or NULL if the node does not exist
 */
dlistint_t *get_dnodeint_at_index(dlistint_t *head, unsigned int index)
{
	unsigned int i = 0;

	while (head)
	{
		if (index == i)
			return (head);
		head = head->next;
		i++;
	}
	return (NULL);
}
