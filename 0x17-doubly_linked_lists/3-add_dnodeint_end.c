#include "lists.h"
#include <stdio.h>
/**
 * add_dnodeint_end - adds a new node at the end
 * @head: head
 * @n: value new node
 * Return: new node adress
 */
dlistint_t *add_dnodeint_end(dlistint_t **head, const int n)
{
	dlistint_t *new = NULL, *aux = *head;

	new = malloc(sizeof(dlistint_t));
	if (!new)
		return (NULL);
	new->n = n;
	new->next = NULL;
	if (*head)
	{
		while (aux->next)
		{
			aux = aux->next;
		}
		aux->next = new;
		new->prev = aux;
	}
	else
	{
		new->prev = NULL;
		*head = new;
	}
	return (new);
}
