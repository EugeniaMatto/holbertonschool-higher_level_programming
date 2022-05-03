#include "lists.h"
/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: head
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	long int i = 0, n = 0, cont = 0;
	char *arr;
	listint_t *aux = *head;

	if (head == NULL || *head == NULL)
		return (1);
	arr = malloc(200);
	while (aux)
	{
		n = aux->n;
		if (n < 0)
			n = -n;
		while (n > 0)
		{
			arr[i] = (n % 10) + '0';
			n = n / 10;
			i++;
		}
		arr[i] = ',';
		i++;
		aux = aux->next;
	}
	arr[i] = ',';
	while (i > cont)
	{
		n = 0;
		while (n < 2)
		{
			if (arr[i - 1] == ',')
				n++;
			i--;
		}
		if (arr[i] == ',')
			i++;
		while (arr[cont] != ',')
		{
			if (arr[cont] != arr[i])
			{
				free(arr);
				return (0);
			}
			cont++;
			i++;
		}
		cont++;
	}
	free(arr);
	return (1);
}
