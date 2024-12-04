%{
#include <stdio.h>
#include <string.h>

int is_valid_url(const char* url);
%}

%%

.*\n { 
    yytext[strcspn(yytext, "\n")] = '\0';

    if (is_valid_url(yytext)) {
        printf("\"%s\" is a valid URL.\n", yytext);
    } else {
        printf("\"%s\" is NOT a valid URL.\n", yytext);
    }
}

%%

// Simple URL validation function
int is_valid_url(const char* url) {
    if (strncmp(url, "http://", 7) == 0 || strncmp(url, "https://", 8) == 0) {
        return 1; // Valid if starts with "http://" or "https://"
    }
    return 0; // Otherwise, not valid
}

int main() {
    printf("Enter a string to validate if it's a URL:\n");
    yylex();
    return 0;
}

int yywrap() {
    return 1;
}