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
                int value = (*head)->value;
                node_t* node = (*head)->next;
                free(*head); // double-frees when list has loop
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
        size_t index = 0;
        bool found = false;
        while (node != NULL && node->value != value) {
                node = node->next;
                index++;
        }

        // if found element, return index of first occurence in list
        if (found)
                return index;
        else
                return -1;
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
        }
        puts("");
}


int main(int argc, char *argv[]) {
        node_t* head = NULL;

        puts("start:");
        show_node(&head); // (empty)

        puts("insert nodes:");
        for (int i = 1; i < argc; i++)
                insert_node(&head, atoi(argv[i]), argc);
        show_node(&head);

        puts("search for node with value 13:");
        if (search_node(&head, 13) > -1)
                printf("13 found at %i\n", search_node(&head, 13));
        else
                puts("13 not found");

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
        while (head != NULL) {
                show_node(&head);
                remove_node(&head, 0);
        }

        puts("removing from empty list");
        remove_node(&head, -1);
        remove_node(&head, 1);
        show_node(&head);
}
