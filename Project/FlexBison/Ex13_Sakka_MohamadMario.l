%{
#include <stdio.h>

int capital_letter_count = 0;  // Counter for capital letters (A-Z)
int whitespace_count = 0;      // Counter for spaces
int newline_count = 0;         // Counter for newlines
int tab_count = 0;             // Counter for tabs

#undef yywrap
#define yywrap() 1
%}

%%

[A-Z]       { capital_letter_count++; }   // Match capital letters
[ ]         { whitespace_count++; }       // Match a space
\n          { newline_count++; }          // Match a newline
\t          { tab_count++; }              // Match a tab
.           { /* Match any other character (ignored) */ }

%%

int main(int argc, char *argv[]) {
    if (argc < 2) {
        printf("Usage: %s <filename>\n", argv[0]);
        return 1;
    }

    FILE *file = fopen(argv[1], "r");
    if (!file) {
        perror("Error opening file");
        return 1;
    }

    yyin = file;  // Set input stream to the file
    yylex();      // Start the lexer

    fclose(file);

    printf("Counts Summary:\n");
    printf("Capital Letters: %d\n", capital_letter_count);
    printf("Whitespaces: %d\n", whitespace_count);
    printf("Newlines: %d\n", newline_count);
    printf("Tabs: %d\n", tab_count);

    return 0;
}
