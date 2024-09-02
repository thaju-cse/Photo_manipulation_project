#include <stdio.h>
#include <cs50.h>
int get_change() {
    int change;
    while (1) {
        printf("Change owed: ");
        if (scanf("%d", &change) == 1 && change >= 0) {
            break;
        } else {
            printf("Please enter a non-negative integer.\n");
            while (getchar() != '\n'); // Clear input buffer
        }
    }
    return change;
}

int calculate_coins(int change) {
    int coins[] = {25, 10, 5, 1};
    int num_coins = 0;

    for (int i = 0; i < sizeof(coins) / sizeof(coins[0]); i++) {
        num_coins += change / coins[i];
        change %= coins[i];
    }

    return num_coins;
}

int main() {
    int change = get_change();
    int num_coins = calculate_coins(change);
    printf("%d\n", num_coins);
    return 0;
}
