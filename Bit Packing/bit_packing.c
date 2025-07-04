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


// BA = Bit Array
// D = Data
// O = Offset
#define PACK(BA, D, O)  (BA = BA | (D << O))
#define READ(BA, O)     ((BA & ((size_t)(pow(2, O) - 1) << O)) >> O)
#define CLEAR(BA, O)    (BA = BA & ~((size_t)(pow(2, O) - 1) << O))


int main(void) {
        // initialize pack to all 0
        uint16_t pack = 0;
        uint8_t data = 0b1101;
        size_t n = 4;
        printf("%016b %08b %i\n", pack, data, n);
        // set packed bits
        PACK(pack, data, n);
        printf("%016b %08b %i\n", pack, data, n);
        // get packed bits
        printf("%016b %08b %i %016b\n", pack, data, n, READ(pack, n));
        // clear packed bits
        CLEAR(pack, n);
        printf("%016b %08b %i\n", pack, data, n);
        return 0;
}
