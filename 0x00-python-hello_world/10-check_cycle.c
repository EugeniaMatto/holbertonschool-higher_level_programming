#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: listint_t
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *head = list;

	if (list == NULL || list->next == NULL)
		return (0);

	while (list != NULL)
	{
		if (list->next == head)
			return (1);
		list = list->next;
	}

	return (0);
}
