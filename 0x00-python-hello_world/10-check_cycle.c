#include "lists.h"
int check(listint_t *list, listint_t *head);
/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: listint_t
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *head = list;

	while (list != NULL)
	{
		if (list->next == head)
			return (1);
		list = list->next;
	}

	return (0);
}
/**
 * check - checks if a singly linked list has a cycle in it
 * @list: listint_t
 * @head: head
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check(listint_t *list, listint_t *head)
{
	int sig = 0;

	while (head && sig < 2)
	{
		if (head->next == list)
			sig++;
		head = head->next;
	}

	if (sig < 2)
		return (1);
	else
		return (0);
}
