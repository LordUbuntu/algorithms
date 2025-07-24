/* Jacobus Burger (2025-07-05)
 * Implementation of a bit field
 * See:
 * - https://en.wikipedia.org/wiki/Bit_field
 * - https://www.gnu.org/software/c-intro-and-ref/manual/html_node/Bit-Field-Packing.html
 */
#include <stdio.h>
#include <stdlib.h>


// Example of a Bit Field in action
#define A 0b01100001
#define B 0b01100010
#define C 0b01100011


int main(int argc, char *argv[]) {
        // get input
        if (argc < 2)
                return 1;
        char letter = argv[1][0];

        // show letter selected
        printf("%c %08b\n", letter, letter);
        printf("%08b %08b %s\n", letter, A, A == letter ? "match" : "");
        printf("%08b %08b %s\n", letter, B, B == letter ? "match" : "");
        printf("%08b %08b %s\n", letter, C, C == letter ? "match" : "");
}
