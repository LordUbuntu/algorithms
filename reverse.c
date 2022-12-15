#include <stdio.h>


void reverse(int* array, int length) {
        for (int i = 0; i < length / 2 + 1; i++) {
                int temp = array[i];
                array[i] = array[length - i - 1];
                array[length - i - 1] = temp;
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
