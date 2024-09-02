#include <cs50.h>
#include <stdio.h>


int main() {
    int n=-1;

    // Prompt the user to enter the number of rows
    while (n<1 )
    {
        n = get_int("Size: ");
    }

    // Iterate through each row
    for (int i = 1; i <= n; i++) {
        // Print spaces
        for (int j = 1; j <= n - i; j++) {
            printf(" ");
        }
        // Print hashes
        for (int k = 1; k <= i; k++) {
            printf("#");
        }
        // Print spaces
        printf("  ");
        // Print hashes
        for (int l = 1; l <= i; l++) {
            printf("#");
        }
        // Move to the next line
        printf("\n");
    }

    return 0;
}
