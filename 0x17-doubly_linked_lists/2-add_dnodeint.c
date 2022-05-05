#include "lists.h"
#include <stdio.h>
/**
 * add_dnodeint - adds a new node at the beginning
 * @head: head
 * @n: value new node
 * Return: new node adress
 */
dlistint_t *add_dnodeint(dlistint_t **head, const int n)
{
	dlistint_t *new = NULL;

	new = malloc(sizeof(dlistint_t));
	if (!new)
		return (NULL);
	new->n = n;
	new->prev = NULL;
	if (*head)
	{
		(*head)->prev = new;
		new->next = *head;
	}
	else
		new->next = NULL;
	*head = new;
	return (new);
}
