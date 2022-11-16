#include <stdio.h>
#include <math.h>

// reverse array of ints
//      swaps every element with its match on the opposite end. O(n/2)
void reverse(int* array, size_t length) {
        int temp;
        for (int i = 0; i < floor(length / 2) + 1; i++) {
                temp = array[i];
                array[i] = array[length - 1 - i];
                array[length - 1 - i] = temp;
                printf("t %i ai %i al %i : i %i l %lu\n", temp, array[i], array[length - 1 - i], i, length);
        }
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
