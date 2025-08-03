/* Jacobus Burger (2025-08-02)
 * Bubble Sort (C99)
 * see:
 * - https://en.wikipedia.org/wiki/Bubble_sort
 */


int* sort(int* array, int length) {
        for (int i = 1; i < length; i++)
                for (int j = 1; j < length; j++)
                        if (array[j - 1] >= array[j]) {
                                // XOR swap
                                array[j - 1] ^= array[j];
                                array[j] ^= array[j - 1];
                                array[j - 1] ^= array[j];
                        }
}
