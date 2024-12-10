%{
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int is_valid_email(const char* email);
%}

%%

.*\n { 
    // Remove the trailing newline
    yytext[strcspn(yytext, "\n")] = '\0';

    if (is_valid_email(yytext)) {
        printf("\"%s\" is a valid email address.\n", yytext);
    } else {
        printf("\"%s\" is NOT a valid email address.\n", yytext);
    }
}

%%

int is_valid_email(const char* email) {
    // Basic checks: must contain '@'
    const char *at_ptr = strchr(email, '@');
    if (!at_ptr) return 0;

    // '@' should not be the first or last character
    if (at_ptr == email || *(at_ptr + 1) == '\0') return 0;

    // Ensure there's only one '@'
    const char *second_at = strchr(at_ptr + 1, '@');
    if (second_at) return 0;  // A second '@' was found

    // Find the last '.' after '@'
    const char *dot_ptr = strrchr(email, '.');
    if (!dot_ptr) return 0; // No '.' found at all
    if (dot_ptr < at_ptr) return 0; // The '.' should be after '@'

    // Check top-level domain length (must have at least 1 char after last dot)
    if (strlen(dot_ptr + 1) <= 1) return 0;

    // Check that there's something between '@' and '.'
    if (dot_ptr == at_ptr + 1) return 0; // no domain name between '@' and '.'

    // If all basic checks passed, consider it valid
    return 1;
}

int main() {
    printf("Enter a string to check if it's an email address:\n");
    yylex();
    return 0;
}

int yywrap() {
    return 1;
}
