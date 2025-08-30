

int fibonacci(int n)
{
        if (n <= 0) {
                return 1;
        }

        int a = 1, b = 1, temp = 0;
        for (size_t i = 0; i < n; i++) {
                temp = b;
                b = a + b;
                a = temp;
        }
        return b;
}
