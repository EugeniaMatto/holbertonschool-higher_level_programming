#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: listint_t
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *aux;

	if (list == NULL)
		return (0);

	aux = list->next;
	while (aux != NULL && aux->next != NULL)
	{
		if (list == aux || list == list->next)
			return (1);

		list = list->next;
		aux = aux->next->next;
	}

	return (0);
}
