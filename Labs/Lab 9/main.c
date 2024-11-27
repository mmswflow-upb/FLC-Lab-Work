#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Function for Task 1: Add two numbers using pointers
void addNumbersUsingPointers() {
    int num1, num2, sum;
    int* ptr1, * ptr2;

    printf("Enter first number: ");
    scanf_s("%d", &num1);  // Use scanf_s instead of scanf_s_f
    printf("Enter second number: ");
    scanf_s("%d", &num2);  // Use scanf_s instead of scanf_s_f

    ptr1 = &num1;
    ptr2 = &num2;

    sum = *ptr1 + *ptr2;

    printf("The sum of %d and %d is %d\n\n", num1, num2, sum);
}

// Function for Task 2: Perform arithmetic operations
void arithmeticOperations() {
    float num1, num2, sum, diff, prod, div, mean;

    printf("Enter first number: ");
    scanf_s("%f", &num1);  // Use scanf_s instead of scanf_s_f
    printf("Enter second number: ");
    scanf_s("%f", &num2);  // Use scanf_s instead of scanf_s_f

    sum = num1 + num2;
    diff = num1 - num2;
    prod = num1 * num2;
    div = (num2 != 0) ? num1 / num2 : 0;
    mean = (num1 + num2) / 2;

    printf("Sum: %.2f\n", sum);
    printf("Difference: %.2f\n", diff);
    printf("Product: %.2f\n", prod);
    if (num2 != 0)
        printf("Division: %.2f\n", div);
    else
        printf("Division: Not possible (division by zero)\n");
    printf("Mean: %.2f\n\n", mean);
}

// Function for Task 3: Check if a number is even or odd
void checkEvenOdd() {
    int num;

    printf("Enter a number: ");
    scanf_s("%d", &num);  // Use scanf_s instead of scanf_s_f

    if (num % 2 == 0)
        printf("%d is Even\n\n", num);
    else
        printf("%d is Odd\n\n", num);
}

// Function for Task 4: Compute the square of a number and call it twice
void computeSquare() {
    int num, result;

    printf("Enter a number: ");
    scanf_s("%d", &num);  // Use scanf_s instead of scanf_s_f

    result = num * num;
    printf("Square of %d: %d\n", num, result);

    result = result * result;
    printf("Square of %d: %d\n\n", num * num, result);
}

void fileOperations() {
    FILE* file;   // Declare the file pointer
    char text[100];

    // Creating and writing to the file
    errno_t err = fopen_s(&file, "example.txt", "w");  // Pass pointer to file
    if (err != 0) {   // fopen_s returns 0 if successful
        printf("Error opening file for writing.\n");
        return;
    }

    printf("Enter text to write into the file (type 'STOP' to end):\n");
    while (1) {
        fgets(text, sizeof(text), stdin);
        if (strncmp(text, "STOP", 4) == 0)
            break;
        fputs(text, file);
    }
    fclose(file);

    // Reading the file content
    err = fopen_s(&file, "example.txt", "r");  // Open the file for reading
    if (err != 0) {  // Check if fopen_s failed
        printf("Error opening file for reading.\n");
        return;
    }

    printf("\nContent of the file:\n");
    while (fgets(text, sizeof(text), file) != NULL) {
        printf("%s", text);  // Print the content of the file
    }
    fclose(file);
    printf("\n");
}

int main() {
    int choice;

    while (1) {
        printf("Choose a task to perform:\n");
        printf("1. Add two numbers using pointers\n");
        printf("2. Perform arithmetic operations\n");
        printf("3. Check if a number is even or odd\n");
        printf("4. Compute the square of a number (called twice)\n");
        printf("5. File operations\n");
        printf("6. Exit\n");
        printf("Enter your choice: ");
        scanf_s("%d", &choice);  // Use scanf_s instead of scanf_s_f
        getchar(); // To consume the newline character after number input

        switch (choice) {
        case 1:
            addNumbersUsingPointers();
            break;
        case 2:
            arithmeticOperations();
            break;
        case 3:
            checkEvenOdd();
            break;
        case 4:
            computeSquare();
            break;
        case 5:
            fileOperations();
            break;
        case 6:
            printf("Exiting the program. Goodbye!\n");
            return 0;
        default:
            printf("Invalid choice. Please try again.\n\n");
        }
    }
}
