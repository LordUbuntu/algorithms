#include <limits.h>
#include <stdlib.h>
#include <stdio.h>


#define MAX(A, B) (A > B ? A : B)


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


void append(node_t** head, int value) {
        // append to empty list
        if (*head == NULL) {
                *head = new_node(value);
                return;
        }

        // append to non-empty list
        node_t* current = *head;
        while (current->next != NULL)
                current = current->next;
        current->next = new_node(value);
}


int truncate(node_t* head) {
        // remove from empty list
        if (head == NULL) {
                return INT_MAX;  // outside usual possibilities
        }

        // remove from list with one element (decapitate)
        if (head->next == NULL) {
                int value = head->value;
                free(head);
                head = NULL;
                return value;
        }

        // remove from list with more than one element (amputate)
        node_t* current = head;
        while (current->next->next != NULL)
                current = current->next;
        int value = current->next->value;
        free(current->next);
        current->next = NULL;
        return value;
}


int main(int argc, char *argv[]) {
        node_t* head = NULL;
        append(&head, 1);
}
