/* Jacobus Burger (2025-07-03)
 * Implemenation of a bit array (a linear sequence of single-bit flags)
 * See:
 * - https://www.cs.emory.edu/%7Echeung/Courses/255/Syllabus/1-C-intro/bit-array.html
 * - https://en.wikipedia.org/wiki/Bit_array
 */
// note for implementation: sizeof can be used to calculate bytes of int
//      type at runtime, and thus can be used to calculate bits per
//      address in array. Then the emory info can be used to produce
//      macros for setting and reading bits along an array
//      This can be used in the sieve_of_eratosthenes.c file!
