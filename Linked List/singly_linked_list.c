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

        struct Node *list;
        struct Node **head = &list;
        struct Node **tail = head;
        for (int i = 2; i < MAX(argc, n); i++) {
                (**tail).value = atoi(argv[i]);
                (**tail).next = &(struct Node){.value = 0, .next = NULL};
                printf("%i, %i\n", (**tail).value, (**tail).next);
                *tail = (**tail).next;
        }
}
