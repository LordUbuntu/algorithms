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

        printf("n: %i\n", n);

        int val = 1;
        if (argc > 2)
                val = atoi(argv[2]);

        struct Node *list;
        struct Node *a;
        struct Node *b;

        list->value = val;
        list->next = a;
        list->next->value = 11;
        list->next->next = b;
        list->next->value = 13;

        printf("%i %i %i\n", list->value, list->next->value, list->next->next->value);

}
