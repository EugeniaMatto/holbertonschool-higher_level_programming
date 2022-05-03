#include "lists.h"
/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: head
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	int cont = 0, i = 0, arr[40];
	listint_t *aux = *head;

	if (head == NULL || *head == NULL)
		return (1);
	while (aux)
	{
		arr[i] = aux->n;
		i++;
		aux = aux->next;
	}
	i = i - 1;
	while (cont < i)
	{
		if (arr[i] != arr[cont])
			return (0);
		i--;
		cont++;
	}
	return (1);
}
