// Jacobus Burger (2025-07-03)
// Implementation of bit packing technique.
// Note: when compiling be sure to link math library. eg:
//      gcc bit_packing.c -lm -o bit_packing
// See:
// - https://www.cs.cornell.edu/courses/cs3410/2024fa/notes/bitpack.html
#include <math.h>
#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>


// P = Bit Pack, D = Data, O = Offset, N = mask size
#define MASK(N)         ( ((size_t)(pow(2, N) - 1) )
#define PACK(P, D, O)   ( P = P | (D << O) )
#define READ(P, N, O)      ( (P & (MASK(N) - 1) << O)) >> O )
#define CLEAR(P, N, O)     ( P = P & ~(MASK(N) - 1) << O) )


int main(int argc, char *argv[]) {
        // get input
        if (argc < 3)
                return 1;
        int data = atoi(argv[1]);
        int n = atoi(argv[2]);

        // show initial state
        uint64_t pack = 0;
        printf("data: %064b %i, offset: %i\n", data, data, n);
        printf("memory: %064b %i\n", pack, pack);
        // set packed bits
        PACK(pack, data, n);
        printf("set memory: %064b %i\n", pack, pack);
        // get packed bits
        printf("get memory: %064b, %i\n", READ(pack, n), READ(pack, n));
        // clear packed bits
        CLEAR(pack, n);
        printf("clear memory: %064b %i\n\n", pack, pack);
        return 0;
}
