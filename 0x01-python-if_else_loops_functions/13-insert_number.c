#include "lists.h"
/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: first node
 * @number: number
 * Return: the adress of the new node or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *aux = *head, *ant = *head, *node;

	new = malloc(sizeof(listint_t));
	new->n = number;
	new->next = NULL;
	node = new;

	if (head == NULL || *head == NULL)
	{
		*head = new;
		return (*head);
	}

	if (!aux->next)
	{
		if (aux->n > number)
			node = NULL;
	}

	while (aux->next && aux->n < number)
	{
		ant = aux;
		aux = aux->next;
	}

	ant->next = node;
	new->next = aux;

	return (new);
}
