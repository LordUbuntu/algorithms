// Jacobus Burger (2025-07-03)
// Implementation of bit packing technique. Just single bits like a
//      packed array of booleans is demonstrated here, but with a simple
//      change it can be extended for a packed segment of any size
//      smaller than the data it is being packed into
// Related concepts seem to be bit arrays which I leive I've implemented
//      here, and bit fields which are a bit different but still related.
// See:
// - https://www.cs.cornell.edu/courses/cs3410/2024fa/notes/bitpack.html
// - https://www.cs.emory.edu/%7Echeung/Courses/255/Syllabus/1-C-intro/bit-array.html
// - https://en.wikipedia.org/wiki/Bit_array
#include <stdio.h>
#include <stdlib.h>
