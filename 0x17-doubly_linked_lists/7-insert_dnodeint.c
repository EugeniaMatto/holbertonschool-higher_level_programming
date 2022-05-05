#include "lists.h"
#include <stdio.h>
/**
 * insert_dnodeint_at_index - adds a new node at the index
 * @h: head
 * @idx: index
 * @n: value new node
 * Return: new node adress
 */
dlistint_t *insert_dnodeint_at_index(dlistint_t **h, unsigned int idx, int n)
{
	dlistint_t *new = NULL, *aux = *h, *sig;
	unsigned int i = 0;

	if (idx == 0 || !(*h) || !h)
		return (add_dnodeint(h, n));

	while (aux && i < (idx - 1))
	{
		aux = aux->next;
		i++;
	}
	if (!aux)
		return (NULL);
	if (aux->next == NULL)
		return (add_dnodeint_end(h, n));

	new = malloc(sizeof(dlistint_t));
	if (!new)
		return (NULL);
	new->n = n;
	sig = aux->next;
	sig->prev = new;
	aux->next = new;
	new->prev = aux;
	new->next = sig;
	return (new);
}
