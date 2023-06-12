#include "lists.h"

/**
 * getprev - get element before adress in p
 * @head: head of list
 * @p: index pointer
 * Return: the pointer before p
 */

listint_t *getprev(listint_t *head, listint_t *p)
{
	listint_t *q;

	for (q = head; q->next != p; q = q->next)
		;

	return (q);
}

/**
 * is_palindrome - if singly list is palindrome
 * @head: head of list
 * Return: 0 or 1
 */

int is_palindrome(listint_t **head)
{
	listint_t *p, *q;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	for (p = *head; p->next != NULL; p = p->next)
		;

	q = *head;

	do {
		if (p->n != q->n)
			return (0);

		p = getprev(*head, p);
		q = q->next;
	} while (p != q && p->next != q);

	return (1);


}

