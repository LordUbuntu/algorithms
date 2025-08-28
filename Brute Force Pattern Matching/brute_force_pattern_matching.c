/* Jacobus Burger (2025-08-23)
 * Brute Force Pattern Matching (C99)
 * Brute Force Pattern Matching is a brute force approach to matching
 *      a substring of a larger string of contiguous data. It does so
 *      by comparing the first letter of the substring with the current
 *      letter in the string until it finds a match, then compares to
 *      see that the substring and that section of the string both
 *      match. This is an obvious approach, but isn't very effective
 *      when compared to more clever approaches.
 * Pattern Matching has a lot of great applications in multiple
 *      disciplines, such as for bioinformatics.
 * Info:
 * - https://en.wikipedia.org/wiki/String-searching_algorithm#Naive_string_search
 * - https://www.youtube.com/watch?v=u6MgvwO8m_8
 * - https://www.youtube.com/watch?v=yKhPWrdA6U8
 */

/* Time Complexity:  O(nm)
 * Space Complexity: O(1)
 */
int match(char *pattern, char *string)
{
        // NOTE: beware string terminator of pattern should be excluded

        // scan across string
        for (size_t n = 0; n <= strlen(string) - strlen(pattern); n++) {
                // check if match found on whole substring
                int found = 1;
                for (size_t m = 0; m < strlen(pattern); m++) {
                        if (pattern[m] != string[n + m]) {
                                found = 0;
                                break;
                        }
                }
                if (found) {
                        return n;
                }
        }
        return -1;  // no match found
}

int main(int argc, char *argv[])
{
        if (argc < 3)
                return 1;
        char *pattern = argv[2];
        char *string = argv[1];
}
