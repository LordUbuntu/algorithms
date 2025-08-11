// Jacobus Burger (2025-06-09)
// Interleaving data of two strings, though the same principle can
//      be applied to any sequence/array data type (though the
//      implementation will differ between them)
// see:
// - https://en.wikipedia.org/wiki/Interleaving_(data)
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MIN(A, B) (A < B ? A : B)


char* interleave(char* a, char* b) {
        size_t memsize = strlen(a) + strlen(b) + 1;
        char* c = (char*) calloc(memsize, sizeof(char));
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
        // make sure args are provided
        if (argc < 3)
                return 1;
        // get a and b from argv
        char* a = argv[1];
        char* b = argv[2];
        // interleave a and b
        char* c = interleave(a, b);
        // print results
        printf("%s\n%s\n%s\n\n\n", a, b, c);
        free(c);  // don't forget to free since it was allocated manually
        return 0;
}
