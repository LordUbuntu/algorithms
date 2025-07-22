/* Jacobus Burger (2025)
 * Singly Linked List implemented in C
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


void insert_node(node_t** head, int value, int index) {
        // insert head node for empty list
        if (*head == NULL) {
                *head = new_node(value);
                return;
        }

        // insert head node for non-empty list
        if (index <= 0) {
                node_t* node = new_node(value);
                node->next = *head;
                *head = node;
                return;
        }

        // insert node to body/tail of non-empty list
        node_t* node = *head;
        for (int i = 0; i < index && node->next != NULL; i++)
                node = node->next;
        node->next = new_node(value);
}


int remove_node(node_t** head, int index) {
        // remove from empty list (return error value INT_MIN)
        if (*head == NULL)
                return INT_MIN;

        // remove head as only element from list
        if ((*head)->next == NULL) {
                int value = (*head)->value;
                free(*head);
                *head = NULL;
                return value;
        }

        // remove from head of non-empty list
        if (index <= 0) {
                // resolve loops
                if ((*head)->next != NULL && (*head)->next->next == *head)
                        (*head)->next->next = NULL;
                // remove head node
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


int search_node(node_t** head, int value) {
        // don't scan empty list
        if (*head == NULL)
                return -1;

        // scan through non-empty list for index of value
        node_t* node = *head;
        node_t* hare = node->next != NULL ? node->next->next : NULL;
        size_t index = 0;
        while (node != hare && node->value != value) {
                node = node->next;
                hare = hare != NULL && hare->next != NULL ? hare->next->next : NULL;
                index++;
        }

        // cycle detected, error value
        if (node == hare)
                return -1;

        // found element, return index of first occurence in list
        return index;
}


void show_node(node_t** head) {
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
                if (node == *head) {
                        printf("(loop)");
                        break;
                }
        }
        puts("");
}


int main(int argc, char *argv[]) {
        node_t* head = NULL;
        show_node(&head); // (empty)
        insert_node(&head, 1, 0);
        insert_node(&head, 2, -1);
        insert_node(&head, 3, 0);
        show_node(&head); // 3 2 1
        printf("r: %i\n", remove_node(&head, -1)); // 3
        printf("r: %i\n", remove_node(&head, 1)); // 1
        show_node(&head); // 2
        insert_node(&head, 4, 5);
        insert_node(&head, 5, 3);
        insert_node(&head, 6, 0);
        show_node(&head); // 6 2 4 5
        printf("s: %i\n", search_node(&head, 0)); // -1
        printf("s: %i\n", search_node(&head, 2)); // 1
        printf("s: %i\n", search_node(&head, 4)); // 2
        // create loop
        node_t* loop = head;
        while (loop->next != NULL)
                loop = loop->next;
        loop->next = head;
        show_node(&head); // 6 2 4 5 (loop)
        // get back to NULL list
        remove_node(&head, 0);
        remove_node(&head, 0); // 1 more than list length to test safety
        remove_node(&head, 0); // 1 more than list length to test safety
        show_node(&head); // (empty)
}
