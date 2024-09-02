#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

// Function to check if the input string consists of only digits
int onlyDigits(char *str) {
    while (*str) {
        if (!isdigit(*str)) {
            return 0;
        }
        str++;
    }
    return 1;
}

// Function to rotate a character by a given number of positions
char rotate(char c, int key) {
    if (isupper(c)) {
        return ((c - 'A' + key) % 26) + 'A';
    } else if (islower(c)) {
        return ((c - 'a' + key) % 26) + 'a';
    } else {
        return c;
    }
}

int main(int argc, char *argv[]) {
    // Check if the correct number of command-line arguments is provided
    if (argc != 2) {
        printf("Usage: ./caesar key\n");
        return 1;
    }

    // Check if the provided key consists of only digits
    if (!onlyDigits(argv[1])) {
        printf("Usage: ./caesar key\n");
        return 1;
    }

    // Convert the key to an integer
    int key = atoi(argv[1]);

    // Prompt the user for plaintext
    printf("plaintext: ");
    char plaintext[1000];
    fgets(plaintext, sizeof(plaintext), stdin);

    // Encrypt the plaintext and print the ciphertext
    printf("ciphertext: ");
    for (int i = 0; plaintext[i] != '\0'; i++) {
        printf("%c", rotate(plaintext[i], key));
    }
    // printf("\n");

    return 0;
}
