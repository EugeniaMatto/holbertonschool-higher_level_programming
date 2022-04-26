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

	if (head == NULL || aux == NULL)
		return NULL;

	new = malloc(sizeof(listint_t));
	new->n = number;
	while (aux->next && aux->n < number)
	{
		ant = aux;
		aux = aux->next;
	}

	ant->next = new;
	new->next = aux;

	return (new);
}
