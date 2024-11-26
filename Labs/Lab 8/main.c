#include <stdio.h>

void checkLeapYear(int year) {
    if ((year % 4 == 0 && year % 100 != 0) || (year % 400 == 0)) {
        printf("%d is a leap year.\n", year);
    }
    else {
        printf("%d is not a leap year.\n", year);
    }
}

void checkNumberSign(int num) {
    switch ((num > 0) - (num < 0)) {
    case 1:
        printf("%d is positive.\n", num);
        break;
    case -1:
        printf("%d is negative.\n", num);
        break;
    case 0:
        printf("%d is zero.\n", num);
        break;
    }
}

void sumOddNumbers() {
    int sum = 0;
    for (int i = 1; i < 20; i += 2) {
        sum += i;
    }
    printf("The sum of odd numbers between 0 and 20 is %d.\n", sum);
}

void countDigits(int num) {
    int count = 0, originalNum = num;
    while (num != 0) {
        num /= 10;
        count++;
    }
    printf("The number %d has %d digits.\n", originalNum, count);
}

void sumArrayElements() {
    int arr[] = { 1, 2, 3, 4, 5 };
    int sum = 0, size = sizeof(arr) / sizeof(arr[0]);
    for (int i = 0; i < size; i++) {
        sum += arr[i];
    }
    printf("The sum of all elements in the array is %d.\n", sum);
}

void findMaximum(int a, int b, int c) {
    if (a > b && a > c) {
        printf("The maximum of %d, %d, %d is %d.\n", a, b, c, a);
    }
    else if (b > c) {
        printf("The maximum of %d, %d, %d is %d.\n", a, b, c, b);
    }
    else {
        printf("The maximum of %d, %d, %d is %d.\n", a, b, c, c);
    }
}

int main() {
    printf("Running all solutions:\n\n");

    int year = 2024;
    printf("1. Leap Year Check:\n");
    checkLeapYear(year);

    int num = -15;
    printf("\n2. Number Sign Check:\n");
    checkNumberSign(num);

    printf("\n3. Sum of Odd Numbers:\n");
    sumOddNumbers();

    int numToCount = 123456;
    printf("\n4. Count Digits:\n");
    countDigits(numToCount);

    printf("\n5. Sum of Array Elements:\n");
    sumArrayElements();

    int a = 10, b = 20, c = 15;
    printf("\n6. Maximum of Three Numbers:\n");
    findMaximum(a, b, c);

    printf("\nAll solutions executed.\n");
    return 0;
}

