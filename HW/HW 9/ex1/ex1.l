%{
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int is_valid_date(const char* date);
%}

%%

.*\n { 
    // Remove the trailing newline character
    yytext[strcspn(yytext, "\n")] = '\0';

    if (is_valid_date(yytext)) {
        printf("\"%s\" is a valid date.\n", yytext);
    } else {
        printf("\"%s\" is NOT a valid date.\n", yytext);
    }
}

%%

// Simple date validation function for format DD/MM/YYYY
int is_valid_date(const char* date) {
    // Check length: "DD/MM/YYYY" should be 10 characters
    // Positions: D(0)D(1)/(2)M(3)M(4)/(5)Y(6)Y(7)Y(8)Y(9)
    if (strlen(date) != 10) {
        return 0;
    }

    // Check the slashes
    if (date[2] != '/' || date[5] != '/') {
        return 0;
    }

    // Extract day, month, and year as strings
    char day_str[3], month_str[3], year_str[5];
    strncpy(day_str, date, 2);
    day_str[2] = '\0';
    strncpy(month_str, date + 3, 2);
    month_str[2] = '\0';
    strncpy(year_str, date + 6, 4);
    year_str[4] = '\0';

    // Convert to integers
    int day = atoi(day_str);
    int month = atoi(month_str);
    int year = atoi(year_str);

    // Basic range checks
    if (month < 1 || month > 12) {
        return 0;
    }

    if (day < 1 || day > 31) {
        return 0;
    }

    // Simple year check (e.g., between 1900 and 2100)
    if (year >= 0) {
        return 0;
    }

    // If all checks pass, consider it a valid date
    return 1;
}

int main() {
    printf("Enter a string to validate if it's a date (DD/MM/YYYY):\n");
    yylex();
    return 0;
}

int yywrap() {
    return 1;
}
