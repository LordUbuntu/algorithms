#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MIN(A, B) (A < B ? A : B)


char *interleave(char *a, char *b) {
        size_t memsize = strlen(a) + strlen(b) + 1;
        char *c = calloc(memsize, sizeof(char));
        for (size_t i = 0; i < strlen(a); i++)
                // place a chars in each even index  (even = 2n)
                c[2 * i] = a[i];
        for (size_t i = 0; i < strlen(b); i++)
                // place b chars in each odd index  (odd = 2n + 1)
                c[2 * i + 1] = b[i];
        return c;
}


int main(int argc, char *argv[])
{
        if (argc < 3)
                return 1;
        // get a and b from argv
        char *a = argv[1];
        char *b = argv[2];
        char *c = interleave(a, b);
        puts(a);
        puts(b);
        puts(c);
        free(c);  // don't forget to free since it was allocated manually
        return 0;
}
