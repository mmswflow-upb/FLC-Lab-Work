#include <stdio.h>
#include <string.h>
#include <stdbool.h>

// Function to search if an element is in an array
bool searchInArray(int arr[], int n, int x) {
    for (int i = 0; i < n; i++) {
        if (arr[i] == x) return true;
    }
    return false;
}

// Function to add two 2D arrays
void add2DArrays(int arr1[2][2], int arr2[2][2], int result[2][2]) {
    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 2; j++) {
            result[i][j] = arr1[i][j] + arr2[i][j];
        }
    }
}

// Function to check if two 2D arrays are equal
bool are2DArraysEqual(int arr1[2][2], int arr2[2][2]) {
    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 2; j++) {
            if (arr1[i][j] != arr2[i][j]) return false;
        }
    }
    return true;
}

// Function to find the length of a string
int stringLength(char str[]) {
    return strlen(str);
}

// Function to search for a word in a string and return its index
int searchWord(char str[], char word[]) {
    char* pos = strstr(str, word);
    if (pos != NULL) {
        return pos - str; // Calculate index
    }
    return -1; // Word not found
}

// Function to check if a string is a palindrome
bool isPalindrome(char str[]) {
    int n = strlen(str);
    for (int i = 0; i < n / 2; i++) {
        if (str[i] != str[n - i - 1]) return false;
    }
    return true;
}

int main() {
    // Task 1: Search if an element is in an array
    int arr[] = { 1, 2, 3, 4, 5 };
    int x = 5;
    if (searchInArray(arr, 5, x)) {
        printf("Element %d is in the array.\n", x);
    }
    else {
        printf("Element %d is not in the array.\n", x);
    }

    // Task 2: Add two 2D arrays
    int arr1[2][2] = { {1, 2}, {3, 4} };
    int arr2[2][2] = { {5, 6}, {7, 8} };
    int result[2][2];
    add2DArrays(arr1, arr2, result);
    printf("Sum of 2D arrays:\n");
    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 2; j++) {
            printf("%d ", result[i][j]);
        }
        printf("\n");
    }

    // Task 3: Check if two 2D arrays are equal
    if (are2DArraysEqual(arr1, arr2)) {
        printf("The 2D arrays are equal.\n");
    }
    else {
        printf("The 2D arrays are not equal.\n");
    }

    // Task 4: Find the length of a string
    char str1[] = "aaa";
    printf("Length of string '%s' is %d.\n", str1, stringLength(str1));

    // Task 5: Search for the word "FILS" and display its index
    char ex[] = "FILS is part of UPB. I am a student at FILS. Welcome!";
    char word[] = "FILS";
    int index = searchWord(ex, word);
    if (index != -1) {
        printf("The word '%s' is found at index %d.\n", word, index);
    }
    else {
        printf("The word '%s' is not found.\n", word);
    }

    // Task 6: Check if a string is a palindrome
    char str2[] = "manam";
    if (isPalindrome(str2)) {
        printf("The string '%s' is a palindrome.\n", str2);
    }
    else {
        printf("The string '%s' is not a palindrome.\n", str2);
    }

    return 0;
}
