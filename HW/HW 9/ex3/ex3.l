%{
#include <stdio.h>
%}

%%

"//".*           { /* matched single-line comment starting with // */ }

"/*"([^*]|\*+[^/])*\*+"/" { /* matched multi-line comments */ }

.|\n             { /* Everything else, just copy it to output */ 
                    fputs(yytext, yyout);  // Write to the output file
                }

%%

int main() {
    // Open the input file for reading (hardcoded file name)
    yyin = fopen("Test.java", "r");
    if (!yyin) {
        perror("fopen input file");
        return 1;
    }

    // Open the output file for writing (hardcoded file name)
    FILE *output_file = fopen("output_file.txt", "w");
    if (!output_file) {
        perror("fopen output file");
        fclose(yyin);
        return 1;
    }

    // Set yyout to the output file
    yyout = output_file;

    // Run the lexer
    yylex();

    // Clean up
    fclose(yyin);
    fclose(output_file);

    return 0;
}

int yywrap() {
    return 1;
}
