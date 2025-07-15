#include <stdlib.h>
#include <stdio.h>


#define MAX(A, B) (A > B ? A : B)


struct Node {
        int value;
        struct Node *next;
};


struct Node *new_node(int value) {
        struct Node *node = (struct Node*) malloc(sizeof(struct Node));
        node->value = value;
        node->next = NULL;
        return node;
}


void delete_node(struct Node *node) {
        free(node);
}


void append_node(struct Node *head, struct Node *node) {
        struct Node *current = head;
        while (current->next != NULL)
                current = current->next;
        current->next = node;
}


int main(int argc, char *argv[]) {
        if (argc < 2)
                return 1;
        int n = atoi(argv[1]);

        printf("n: %i\n", n);

        struct Node *head;
        struct Node *a = new_node(13);
        struct Node *b = new_node(31);
        struct Node *c = new_node(131);
        head = a;
        append_node(head, b);
        append_node(head, c);
        printf("%i: %i %i %i\n", &a, a->value, a->next, a->next ? a->next->value : 0);
        printf("%i: %i %i %i\n", &b, b->value, b->next, b->next ? b->next->value : 0);
        printf("%i: %i %i %i\n", &c, c->value, c->next, c->next ? c->next->value : 0);
        delete_node(a);
        delete_node(b);
        delete_node(c);
}
