// Jacobus Burger (2023)
// binary search on an array of values, O(log n) time
// see: https://en.wikipedia.org/wiki/Binary_search_algorithm
int
search(int target, int *array, int length)
{
        int left = 0, right = length - 1;
        while (left <= right)
        {
                int middle = (left + right) / 2;
                if (target == array[middle])
                {
                        return middle;
                }
                else if (target > array[middle])
                {
                        left = middle + 1;
                }
                else if (target < array[middle])
                {
                        right = middle - 1;
                }
        }
        return -1;
}
