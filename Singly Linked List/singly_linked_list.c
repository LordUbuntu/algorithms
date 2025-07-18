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


void insert_head(node_t** head, int value) {
        // prepend to empty list
        if (*head == NULL) {
                *head = new_node(value);
                return;
        }

        // prepend to non-empty list
        node_t* node = new_node(value);
        node->next = *head;
        *head = node;
}


void insert_tail(node_t** head, int value) {
        // append to empty list
        if (*head == NULL) {
                *head = new_node(value);
                return;
        }

        // append to non-empty list
        node_t* node = *head;
        while (node->next != NULL)
                node = node->next;
        node->next = new_node(value);
}


void insert(node_t** head, int value, int index) {
        // append to empty list
        if (*head == NULL) {
                *head = new_node(value);
                return;
        }

        // append to non-empty list until before index
        node_t* node = *head;
        for (int i = 0; i < index && node->next != NULL; i++)
                node = node->next;
        node->next = new_node(value);
}


int remove_head(node_t** head) {
        if (*head == NULL)
                return INT_MIN;

        int value = (*head)->value;
        node_t* node = (*head)->next;
        free(*head);
        *head = node;
}


int remove_tail(node_t** head) {
        // remove from empty list (return error value INT_MIN)
        if (*head == NULL)
                return INT_MIN;

        // remove from list with one element (decapitate)
        if ((*head)->next == NULL) {
                int value = (*head)->value;
                free(*head);
                *head = NULL;
                return value;
        }

        // remove from list with more than one element (amputate)
        node_t* node = *head;
        while (node->next->next != NULL)
                node = node->next;
        int value = node->next->value;
        free(node->next);
        node->next = NULL;
        return value;
}


// TODO:
int remove(node_t** head, int value, int index);


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
