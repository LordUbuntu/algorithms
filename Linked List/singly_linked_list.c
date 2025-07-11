#include <stdlib.h>
#include <stdio.h>


struct Node {
        int value;
        Node* next;
};


int main(int argc, char *argv[]) {
        if (argc < 2)
                return 1;
        int n = atoi(argv[1]);
        for (int i = 2; i < argc && i < n; i++)
                // TODO: add append/insert
                printf("%i ", atoi(argv[i]));
        // TODO: more logic to add
}
