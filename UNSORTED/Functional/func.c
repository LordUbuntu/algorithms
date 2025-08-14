#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
/* functional(ish) C programming demo
 *
 * These principles are applied:
 * + Pure functions over impure functions
 * + Stateless and immutable over global state and mutable
 * + Static typing and type conversions over type coercions
 *
 * This is still C though, so these principles while followed carefully depend
 * on what is being done and why. For instance, functions are pure, but memory
 * may be modified rather than copied under the hood.
 *
 * By applying the preferences and designs for pure functions and minimized
 * state the code will be more predictable and maintainable.
 */



// standard functions
int add(int a, int b) {
        return a + b;
}
int sub(int a, int b) {
        return a - b;
}
int mul(int a, int b) {
        return a * b;
}
int div(int a, int b) {
        return a / b;
}
int pow(int a, int n) {
        return a ^ n;
}



// ADT
typedef void* any;
typedef struct {any result; int error;} option;



// higher order functions
void filter(bool (*f)(int), int *A, int *B, size_t length) {
        // preconditions:
        //      length is same for A and B
        //      A is the values to filter
        //      B is the filtered results ending with a null terminator
        int i = 0;
        while (i < length) {
                if ((*f)(A[i])) {
                        B[i] = A[i];
                        i++;
                }
        }
        if (i < length - 1)
                B[i + 1] = NULL;
}
void map(int (*f)(int, int), int *A, int *B, int *C, size_t length) {
        // take a func f and 2 arrays A and B and map result into C
        for (size_t i = 0; i < length; i++)
                C[i] = (*f)(A[i], B[i]);
}
int reduce(int (*f)(int, int), int *A, size_t length) {
        // take a func f applied to A and return the accumulated result
        accumulator = A[0];
        for (size_t i = 1; i < length; i++)
                accumulator = (*f)(accumulator, A[i]);
        return accumulator;
}



int main(void) {
        // demo higher order functions
        int A[5] = {1, 2, 3, 4, 5};
        int B[5] = {2, 2, 2, 2, 2};
        int C[5] = {0};

        puts("original lists:");
        printf("%c: %i %i %i %i %i\n", 'A', A[0], A[1], A[2], A[3], A[4]);
        printf("%c: %i %i %i %i %i\n", 'B', B[0], B[1], B[2], B[3], B[4]);
        printf("%c: %i %i %i %i %i\n\n", 'C', C[0], C[1], C[2], C[3], C[4]);

        map(&add, A, B, C, 5);

        puts("lists with add function:");
        printf("%c: %i %i %i %i %i\n", 'A', A[0], A[1], A[2], A[3], A[4]);
        printf("%c: %i %i %i %i %i\n", 'B', B[0], B[1], B[2], B[3], B[4]);
        printf("%c: %i %i %i %i %i\n\n", 'C', C[0], C[1], C[2], C[3], C[4]);

        map(&mul, A, B, C, 5);

        puts("lists with product function:");
        printf("%c: %i %i %i %i %i\n", 'A', A[0], A[1], A[2], A[3], A[4]);
        printf("%c: %i %i %i %i %i\n", 'B', B[0], B[1], B[2], B[3], B[4]);
        printf("%c: %i %i %i %i %i\n\n", 'C', C[0], C[1], C[2], C[3], C[4]);

        printf("reduce add of A: %i\n\n", reduce(&add, A, 5));


}
