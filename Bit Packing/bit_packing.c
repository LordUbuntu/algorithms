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
// PACK or's data D into bit pack P at offset O.
//      clearing the section to store new data is required.
// READ unpacks N bits from bit pack P at offset O
// CLEAR zeroes out N bits from bit pack P at offset O
#define MASK(N)         ( ((size_t)pow(2, N)) - 1 )
// NOTE: this may be able to be done without clear using triple XOR
#define PACK(P, D, O)   ( P |= (D << O) )
#define READ(P, N, O)   ( (P & (MASK(N) << O)) >> O )
#define CLEAR(P, N, O)  ( P &= ~(MASK(N) << O) )


int main(int argc, char *argv[]) {
        // get input
        if (argc < 3)
                return 1;
        uint8_t data = atoi(argv[1]);
        size_t o = atoi(argv[2]);

        // show initial state
        uint64_t pack = 0;
        printf("data: %08b %i, offset: %i\n", data, data, o);
        printf("memory: %064b %i\n", pack, pack);
        // set packed bits
        PACK(pack, data, o);
        printf("set memory: %064b %i\n", pack, pack);
        // get packed bits
        printf("get memory: %064b, %i\n", READ(pack, 4, o), READ(pack, 4, o));
        // clear packed bits
        CLEAR(pack, 4, o);
        printf("clr memory: %064b %i\n\n", pack, pack);
        return 0;
}
