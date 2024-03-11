#ifndef LIST_H_
#define LIST_H_

#include<stdlib.h>
#include<stdio.h>

typedef struct listnode_s
{
	int i;
	struct listnode_s *next;
} listnode_t;

/**function**/
size_t print_listnode(const listnode_t *h);
listnode_t *add_nodeint(listnode_t **head, const int n);
void free_listnode(listnode_t *head);
int check_cycle(listnode_t *list);

#endif /* LIST_H_ */

