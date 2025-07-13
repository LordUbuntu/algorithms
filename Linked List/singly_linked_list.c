#include <stdlib.h>
#include <stdio.h>


#define MAX(A, B) (A > B ? A : B)


struct Node {
        int value;
        struct Node *next;
};


int main(int argc, char *argv[]) {
        if (argc < 2)
                return 1;
        int n = atoi(argv[1]);

        struct Node *list = &(struct Node*){1, NULL};
        struct Node **head = &list;
        struct Node **current = head;
        for (int i = 2; i < MAX(argc, n); i++) {
                (*current).value = 
                struct Node *head = &(struct Node){1, NULL};
        }
        printf("%i, %i\n", (*head).value, (*head).next);
}
