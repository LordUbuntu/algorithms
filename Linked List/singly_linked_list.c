#include <stdlib.h>
#include <stdio.h>


#define MAX(A, B) (A > B ? A : B)


typedef struct node {
        int value;
        struct node* next;
} node_t;


void append(node_t* head, int value) {
        // prepare new node (alloc)
        node_t* node = (node_t*) malloc(sizeof(node_t));
        node->value = value;
        node->next = NULL;

        // append to empty list
        if (head == NULL) {
                head = node;
                return;
        }

        // append to non-empty list
        node_t* current = head;
        while (current->next != NULL)
                current = current->next;
        current->next = node;
}


int truncate(node_t* head) {
        int value = 0;

        // return early if already empty
        if (head == NULL)
                return value;

        // empty list if head is only node
        if (head->next == NULL) {
                value = head->value;
                free(head);
                head = NULL;
                return value;
        }

        // remove tail node
        node_t* current = head;
        while (current->next->next != NULL)
                current = current->next;
        value = current->next->value;
        free(current->next);
        current->next = NULL;
        return value;
}


void show(node_t* head) {
        node_t* current = head;
        while (current != NULL) {
                printf("%i ", current->value);
                current = current->next;
        }
}


int main(int argc, char *argv[]) {
        node_t* list = NULL;  // required in this implementation
        append(list, 1);
        append(list, 2);
        append(list, 3);
        show(list);
        truncate(list);
}
