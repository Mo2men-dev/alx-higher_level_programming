#include "lists.h"

/**
 * check_cycle - function to check cycle in a linked list
 * @list: pointer to the head of the linked list
 *
 * Return: 1 if there is a cycle 0 otherwise.
*/
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
			return (1);
	}

	return (0);
}
