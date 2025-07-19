/* Jacobus Burger (2025)
 * Singly Linked List implemented in C
 *
 * See:
 * - https://en.wikipedia.org/wiki/Linked_list
 * - https://www.learn-c.org/en/Linked_lists
 */
#include <limits.h>
#include <stdlib.h>
#include <stdio.h>
// there doesn't seem to be a single universal implemenation of a singly linked list, there's some with more and some with less functions. So for the sake of simplicity, I'll think about having just insert, remove, and search functions.


typedef struct node {
        int value;
        struct node* next;
} node_t;


node_t* new_node(int value) {
        node_t* node = (node_t*) malloc(sizeof(node_t));
        node->value = value;
        node->next = NULL;
        return node;
}


void insert(node_t** head, int value, int index) {
        // append to empty list
        if (*head == NULL) {
                *head = new_node(value);
                return;
        }

        // append to head of non-empty list
        if (index < 0) {
                node_t* node = new_node(value);
                node->next = *head;
                *head = node;
                return;
        }

        // append to non-empty list until before index
        node_t* node = *head;
        for (int i = 0; i < index && node->next != NULL; i++)
                node = node->next;
        node->next = new_node(value);
}


int remove(node_t** head, int value, int index) {
        // remove from empty list (return error value INT_MIN)
        if (*head == NULL)
                return INT_MIN;

        // remove from head of non-empty list
        if (index <= 0) {
                int value = (*head)->value;
                node_t* node = (*head)->next;
                free(*head);
                *head = node;
                return value;
        }

        // remove from body/tail of non-empty list
        node_t* node = *head;
        for (int i = 0; i < index && node->next->next != NULL; i++)
                node = node->next;
        int value = node->next->value;
        free(node->next);
        node->next = NULL;
        return value;
}


int search(node_t** head, int value); // TODO:


void show(node_t** head) {
        // show empty list
        if (*head == NULL) {
                printf("(empty)\n");
                return;
        }

        // show non-empty list
        node_t* node = *head;
        while (node != NULL) {
                printf("%i ", node->value);
                node = node->next;
        }
        puts("");
}


int main(int argc, char *argv[]) {
        node_t* head = NULL;
        show(&head);
        insert_head(&head, 1);
        insert_head(&head, 2);
        show(&head);
        insert_tail(&head, 3);
        insert_tail(&head, 4);
        show(&head);
        remove_head(&head);
        show(&head);
        remove_tail(&head);
        show(&head);
        remove_tail(&head);
        remove_tail(&head);
        remove_tail(&head);
        show(&head);
        insert_head(&head, 13);
        show(&head);
        remove_head(&head);
        show(&head);
        remove_head(&head);
        show(&head);
}
