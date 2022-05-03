#include "lists.h"
/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: head
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	int cont = 0, i = 0;
	listint_t *aux = *head, *med = *head;

	if (head == NULL || *head == NULL)
		return (1);
	while (aux->next)
	{
		cont++;
		if (aux->n == aux->next->n)
			break;
		aux = aux->next;
	}
	if (aux->next == NULL)
		return (0);
	aux = aux->next;
	while(aux)
	{
		i = 0;
		med = *head;
		while(i < cont - 1)
		{
			med = med->next;
			i++;
		}
		if(aux->n != med->n)
			return (0);
		aux = aux->next;
		cont--;
	}
	return (1);
}
