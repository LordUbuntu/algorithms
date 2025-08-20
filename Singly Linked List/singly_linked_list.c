/* Jacobus Burger (2025-07-17)
 * Singly Linked List (C99)
 * A Singly Linked List is a collection of data where each element
 *      in the sequence points to the next element. It allows for easy
 *      insertion and deletion of data in the sequence without requiring
 *      reorganization or reallocation of the entire structure to do so,
 *      the tradeoff is linear time to access data since each node in the
 *      list must be accessed in sequence.
 * See:
 * - https://en.wikipedia.org/wiki/Linked_list
 * - https://www.learn-c.org/en/Linked_lists
 */
#include <limits.h>
#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>


/* Node Abstract Data Structure (ADS)
 * int value: the value being stored in this node in the list.
 * struct node *next: a reference / link to the next node in the list.
 */
typedef struct {
        int value;
        struct node *next;
} node_t;


/* Time Complexity: O(1)
 * Space Complexity: O(1)
 */
node_t* new_node(int value)
{
        node_t *node = (node_t*) malloc(sizeof(node_t));
        node->value = value;
        node->next = NULL;
        return node;
}


/* Time Complexity: O(n)
 * Space Complexity: O(1)
 */
void insert_node(node_t **head, int index, int value)
{
        node_t *node = new_node(value);

        // insert head node for empty list
        if (!*head) {
                *head = node;
                return;
        }

        // insert head node for non-empty list
        if (index <= 0) {
                node->next = *head;
                *head = node;
                return;
        }

        // insert node to body/tail of non-empty list
        node_t *current = *head;
        for (int i = 0; current->next && i < index; i++) {
                current = current->next;
        }
        if (!current->next) {
                current->next = node;
                return;
        }
        node_t *temp = current->next;
        current->next = node;
        node->next = temp;
}


/* Time Complexity: O(n)
 * Space Complexity: O(1)
 */
int remove_node(node_t **head, int index)
{
        // remove from empty list (return error value INT_MIN)
        if (!*head) {
                return INT_MIN;
        }

        // remove head as only element from list
        if (!(*head)->next) {
                int value = (*head)->value;
                free(*head);
                *head = NULL;
                return value;
        }

        // remove from head of non-empty list
        if (index <= 0) {
                node_t *prev = *head;
                int value = prev->value;
                *head = prev->next;
                prev->next = NULL;
                free(prev);
                return value;
        }

        // remove from body/tail of non-empty list
        node_t *current = *head;
        for (int i = 0; current->next->next && i < index; i++) {
                current = current->next;
        }
        node_t *next = current->next;
        int value = next->value;
        current->next = next->next;
        next->next = NULL;
        free(next);
        return value;
}


/* Time Complexity: O(n)
 * Space Complexity: O(1)
 */
int find_node(node_t **head, int value)
{
        // don't scan empty list
        if (!*head) {
                return -1;
        }

        // scan through non-empty list for index of value
        node_t *current = *head;
        size_t index = 0;
        while (current) {
                if (current->value == value) {
                        return index;
                }
                current = current->next;
                index++;
        }
        return -1;
}


/* Time Complexity: O(n)
 * Space Complexity: O(1)
 */
int peek_node(node_t **head, int index)
{
        // don't peek empty list
        if (!*head) {
                return INT_MIN;
        }

        // peek for a node in a non-empty list
        node_t *current = *head;
        for (int i = 0; current->next; i++) {
                if (i == index) {
                        return current->value;
                }
                current = current->next;
        }
        return INT_MIN;
}


/* Time Complexity: O(n)
 * Space Complexity: O(1)
 */
void show_node(node_t **head)
{
        // show empty list
        if (!*head) {
                printf("(empty)\n");
                return;
        }

        // show non-empty list
        node_t *node = *head;
        while (node) {
                printf("%i ", node->value);
                node = node->next;
        }
        puts("");
}


int main(void)
{
        node_t *head = NULL;

        puts("start:");
        show_node(&head); // (empty)

        puts("insert nodes:");
        #define LEN 14
        for (int i = 1; i < LEN; i++) {
                insert_node(&head, LEN, i);
        }
        show_node(&head);

        printf("search for node with value 7: %i\n", find_node(&head, 7));

        printf("peek node at index 2: %i\n", peek_node(&head, 2));

        puts("remove from head:");
        printf("value: %i\n", remove_node(&head, -1));
        show_node(&head);

        puts("remove from tail:");
        printf("value: %i\n", remove_node(&head, 1));
        show_node(&head);


        puts("remove from end of tail:");
        printf("value: %i\n", remove_node(&head, LEN));
        show_node(&head);


        puts("removing all nodes:");
        while (head) {
                show_node(&head);
                remove_node(&head, 0);
        }

        puts("removing from empty list");
        remove_node(&head, -1);
        remove_node(&head, 1);
        show_node(&head);
}
