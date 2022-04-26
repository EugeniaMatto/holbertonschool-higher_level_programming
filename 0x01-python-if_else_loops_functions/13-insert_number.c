#include "lists.h"
/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: first node
 * @number: number
 * Return: the adress of the new node or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new = NULL, *aux = *head, *ant = NULL;

	while (aux && aux->n < number)
	{
		ant = aux;
		aux = aux->next;
	}

	if (aux->next == NULL)
		add_nodeint_end(head, number);

	new = malloc(sizeof(listint_t));
	new->n = number;
	new->next = NULL;

	if (ant == NULL)
	{
		if (aux->n > number)
			new->next = aux;
		else
			aux->next = new;
	}
	else
	{
		ant->next = new;
		new->next = aux;
	}

	return (new);
}
