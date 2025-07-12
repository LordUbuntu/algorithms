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
        for (int i = 2; i < MAX(argc, n); i++)
                printf("%i ", atoi(argv[i]));
        struct Node node = {1, NULL};
        struct Node *head = &node;
        printf("%i, %i\n", (*head).value, (*head).next);
}
