/* Jacobus Burger (2022)
 *
 * Info:
 *      I wondered about a fast way to reverse an array of elements
 *      and imagined iterating halfway across the array and then
 *      swapping the current element with its "mirror".
 * Explanation:
 *      The algorithm works by iterating through half the length of
 *      the array, it then swaps the current element with its
 *      "mirror" (the current index from the length of the whole array).
 *      This results in swapping all the elements swapping in what
 *      I approximate to be O(n/2) time.
 */
#include <stdio.h>


void reverse(int* array, int length) {
        for (int i = 0; i < length / 2 + 1; i++) {
                int temp = array[i];
                array[i] = array[length - i - 1];
                array[length - i - 1] = temp;
        }
}


void print_array(int* array, int length) {
        for (int i = 0; i < length; i++)
                printf("%i ", array[i]);
        printf("\n");
}


char equals_array(int* A, int A_length, int* B, int B_length) {
        if (A_length != B_length)
                return 0;
        for (int i = 0; i < A_length; i++)
                if (A[i] != B[i])
                        return 0;
        return 1;
}


int main(void) {
        #define LEN 16
        int a[LEN] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16};
        reverse(a, LEN);
        for (int i = 0; i < LEN; i++) {
                printf("%i ", a[i]);
        }
        printf("\n");
}
