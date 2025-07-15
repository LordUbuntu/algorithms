#include <stdlib.h>
#include <stdio.h>


#define MAX(A, B) (A > B ? A : B)


struct node {
        int value;
        struct node* next;
} node_t;


void append(node_t* head, int value) {
        node_t* current = head;
        while (current->next != NULL)
                current = current->next;

        current->next = (node_t*) malloc(sizeof(node_t));
        current->next->value = value;
        current->next->next = NULL;
}


int main(int argc, char *argv[]) {
        if (argc < 2)
                return 1;
        int n = atoi(argv[1]);

        printf("n: %i\n", n);
}
