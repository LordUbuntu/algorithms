// Jacobus Burger (2025-07-03)
// Implementation of bit packing technique.
// Related concepts seem to be bit arrays which I leive I've implemented
//      here, and bit fields which are a bit different but still related.
// See:
// - https://www.cs.cornell.edu/courses/cs3410/2024fa/notes/bitpack.html
// - https://www.cs.emory.edu/%7Echeung/Courses/255/Syllabus/1-C-intro/bit-array.html
// - https://en.wikipedia.org/wiki/Bit_array
#include <stdio.h>
#include <stdint.h>


int main(void) {
        // initialize pack to all 0
        uint8_t pack = 0;
        printf("%032b\n", pack);
        // set packed bits
        set_bit(pack, n);
        printf("%032b\n", pack);
        // get packed bits
        printf("%032b %032b\n", pack, get_bit(pack, n));
        // clear packed bits
        clear_bit(pack, n);
        printf("%032b\n", pack);
        return 0;
}
