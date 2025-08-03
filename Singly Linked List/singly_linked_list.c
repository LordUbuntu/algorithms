/* Jacobus Burger (2025-07-17)
 * Singly Linked List
 * See:
 * - https://en.wikipedia.org/wiki/Linked_list
 * - https://www.learn-c.org/en/Linked_lists
 */
#include <limits.h>
#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>


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


void insert_node(node_t** head, int index, int value) {
        node_t* node = new_node(value);

        // insert head node for empty list
        if (!*head) {
                *head = node;
                return;
        }

        // insert head node for non-empty list
        if (index <= 0) {
                node->next = *head;
                *head = node;
                return;
        }

        // insert node to body/tail of non-empty list
        node_t* current = *head;
        for (int i = 0; current->next && i < index; i++)
                current = current->next;
        if (!current->next) {
                current->next = node;
                return;
        }
        node_t* temp = current->next;
        current->next = node;
        node->next = temp;
}


int remove_node(node_t** head, int index) {
        // remove from empty list (return error value INT_MIN)
        if (!*head)
                return INT_MIN;

        // remove head as only element from list
        if (!(*head)->next) {
                int value = (*head)->value;
                free(*head);
                *head = NULL;
                return value;
        }

        // remove from head of non-empty list
        if (index <= 0) {
                node_t* prev = *head;
                int value = prev->value;
                *head = prev->next;
                prev->next = NULL;
                free(prev);
                return value;
        }

        // remove from body/tail of non-empty list
        node_t* current = *head;
        for (int i = 0; current->next->next && i < index; i++)
                current = current->next;
        node_t* next = current->next;
        int value = next->value;
        current->next = next->next;
        next->next = NULL;
        free(next);
        return value;
}


int find_node(node_t** head, int value) {
        // don't scan empty list
        if (!*head)
                return -1;

        // scan through non-empty list for index of value
        node_t* current = *head;
        size_t index = 0;
        while (current) {
                if (current->value == value)
                        return index;
                current = current->next;
                index++;

        }
        return -1;
}


int peek_node(node_t** head, int index) {
        // don't peek empty list
        if (!*head)
                return INT_MIN;

        // peek for a node in a non-empty list
        node_t* current = *head;
        for (int i = 0; current->next; i++) {
                if (i == index)
                        return current->value;
                current = current->next;
        }
        return INT_MIN;
}


void show_node(node_t** head) {
        // show empty list
        if (!*head) {
                printf("(empty)\n");
                return;
        }

        // show non-empty list
        node_t* node = *head;
        while (node) {
                printf("%i ", node->value);
                node = node->next;
        }
        puts("");
}


int main(int argc, char *argv[]) {
        node_t* head = NULL;

        puts("start:");
        show_node(&head); // (empty)

        puts("insert nodes:");
        for (int i = 1; i < argc; i++)
                insert_node(&head, argc, atoi(argv[i]));
        show_node(&head);

        printf("search for node with value 13: %i\n", find_node(&head, 13));

        printf("peek node at index 2: %i\n", peek_node(&head, 2));

        puts("remove from head:");
        printf("value: %i\n", remove_node(&head, -1));
        show_node(&head);

        puts("remove from tail:");
        printf("value: %i\n", remove_node(&head, 1));
        show_node(&head);


        puts("remove from end of tail:");
        printf("value: %i\n", remove_node(&head, INT_MAX - 1));
        show_node(&head);


        puts("removing all nodes:");
        while (head) {
                show_node(&head);
                remove_node(&head, 0);
        }

        puts("removing from empty list");
        remove_node(&head, -1);
        remove_node(&head, 1);
        show_node(&head);
}
