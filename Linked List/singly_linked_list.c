#include <stdlib.h>
#include <stdio.h>


#define MAX(A, B) (A > B ? A : B)


typedef struct node {
        int value;
        struct node* next;
} node_t;


void append(node_t* head, int value) {
        // append to empty list
        if (head == NULL) {
                head = (node_t*) malloc(sizeof(node_t));
                head->value = value;
                head->next = NULL;
                return;
        }

        // append to non-empty list
        node_t* current = head;
        while (current->next != NULL)
                current = current->next;
        current->next = (node_t*) malloc(sizeof(node_t));
        current->next->value = value;
        current->next->next = NULL;
}


int truncate(node_t* head) {
        int value = 0;

        // empty list if head is only node
        if (head->next == NULL) {
                value = head->value;
                free(head);
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
        if (argc < 2)
                return 1;
        int n = atoi(argv[1]);

        printf("n: %i\n", n);
        node_t* list;
        printf("list is: %s\n", list == NULL ? "T" : "F");
}
