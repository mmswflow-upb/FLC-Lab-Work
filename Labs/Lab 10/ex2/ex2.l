%{
#include <stdio.h>
int line_number = 1; 
%}

%%
[^\n]+    { fprintf(yyout, "%d %s\n", line_number++, yytext); }

%%

int yywrap(){}
int main() {
    yyin = fopen("in", "r");   // Open the input file for reading
    if (!yyin) {
        perror("Error opening input file");
        return 1;
    }

    yyout = fopen("out", "w"); // Open the output file for writing
    if (!yyout) {
        perror("Error opening output file");
        fclose(yyin);
        return 1;
    }

    yylex(); // Start processing the input

    fclose(yyin);
    fclose(yyout);
    return 0;
}