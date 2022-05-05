#include "lists.h"
#include <stdio.h>
/**
 * free_dlistint - frees a dlistint_t list.
 * @head: head
 * Return: void
 */
void free_dlistint(dlistint_t *head)
{
	dlistint_t *aux;

	if (head)
	{
		while (head)
		{
			aux = head->next;
			free(head);
			head = aux;
		}
	}
}
