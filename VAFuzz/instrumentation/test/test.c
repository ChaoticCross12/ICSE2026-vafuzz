#include <stdio.h>

int main(int argc, char *argv[]) {
    // Print the program name
    printf("Program Name: %s\n", argv[0]);

    // Print the command-line arguments
    printf("Command-Line Arguments:\n");
    for (int i = 1; i < argc; i++) {
        printf("argv[%d]: %s\n", i, argv[i]);
    }

    return 0;
}
