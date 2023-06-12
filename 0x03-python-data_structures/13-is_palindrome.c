#include "lists.h"
#include <stdio.h>

/**
 * reverse - end to middle orientation
 * @h: middle head
 * Return: nothing
 */

void reverse(listint_t **h)
{
	listint_t *p, *q, *cur;

	p = NULL;
	cur = *h;

	while (cur != NULL)
	{
		q = cur->next;
		cur->next = p;
		p = cur;
		cur = q;
	}

	*h = p;
}

/**
 * palin - check if is palin
 * @h1: first head
 * @h2: second head
 * Return: 1 or 0
 */

int palin(listint_t *h1, listint_t *h2)
{
	listint_t *p;
	listint_t *q;

	p = h1;
	q = h2;

	while (p != NULL && q != NULL)
	{
		if (p->n != q->n)
			return (0);
		p = p->next;
		q = q->next;
	}

	if (p == NULL && q == NULL)
		return (1);
	return (0);
}

/**
 * is_palindrome - if singly list is palindrome
 * @head: head of list
 * Return: 0 or 1
 */

int is_palindrome(listint_t **head)
{
	listint_t *p, *q, *prev, *h2, *middle = NULL;
	int k = 1;

	p = *head;
	q = *head;
	prev = *head;

	if (*head != NULL && (*head)->next != NULL)
	{
		while (q != NULL && q->next != NULL)
		{
			q = q->next->next;
			prev = p;
			p = p->next;
		}

		if (q != NULL)
		{
			middle = p;
			p = p->next;
		}

		h2 = p;
		prev->next = NULL;

		reverse(&h2);
		k = palin(*head, h2);

		reverse(&h2);

		if (middle != NULL)
		{
			prev->next = middle;
			prev = prev->next;
		}

		prev->next = h2;
	}

	return (k);
}
