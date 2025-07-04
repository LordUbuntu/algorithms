// Jacobus Burger (2025-07-03)
// Implementation of bit packing technique.
// Related concepts seem to be bit arrays which I leive I've implemented
//      here, and bit fields which are a bit different but still related.
// Note: is should be weary of endianness.
// note: when compiling be sure to link math library. eg:
//      gcc bit_packing.c -lm -o bit_packing
// See:
// - https://www.cs.cornell.edu/courses/cs3410/2024fa/notes/bitpack.html
// - https://www.cs.emory.edu/%7Echeung/Courses/255/Syllabus/1-C-intro/bit-array.html
// - https://en.wikipedia.org/wiki/Bit_array
#include <math.h>
#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>


// BA = Bit Array
// D = Data
// O = Offset
#define PACK(BA, D, O)  (BA = BA | (D << O))
#define READ(BA, O)     ((BA & ((size_t)(pow(2, O) - 1) << O)) >> O)
#define CLEAR(BA, O)    (BA = BA & ~((size_t)(pow(2, O) - 1) << O))


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
