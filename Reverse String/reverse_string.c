/* Jacobus Burger (2025-08-21)
 * Reverse a string (C99)
 * Description:
 * Reverse characters in a string. The principles behind this can
 *   be generalized on a string of any data type (strings do not
 *   have to be a string of characters).
 * There's many approaches to doing this. One approach is to modify
 *   an existing array provided, another is to create and return a new
 *   array, and more.
 * Info:
 * - https://en.wikipedia.org/wiki/String_(computer_science)#Reversal
 * - https://rosettacode.org/wiki/Reverse_a_string
 */
#include <stdio.h>
#include <string.h>


/* Time Complexity: O(n)
 * Space Complexity: O(1)
 */
char* reverse(char *string, size_t length)
{
        return string;
}


int main(int argc, char *argv[])
{
        if (argc < 2) {
                return 1;
        }
        char *string = argv[1];
        printf("%s\n", string);

        char *result = reverse(string, strlen(string));
        printf("%s\n", result);
}
