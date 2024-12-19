%{
#include <stdio.h>

int capital_letter_count = 0;  
int whitespace_count = 0;     
int newline_count = 0;         
int tab_count = 0;             

#undef yywrap
#define yywrap() 1
%}

%%

[A-Z]       { capital_letter_count++; }   
[ ]         { whitespace_count++; }      
\n          { newline_count++; }          
\t          { tab_count++; }              
.           {  }

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

    yyin = file; 
    yylex();     

    fclose(file);

    printf("Counts Summary:\n");
    printf("Capital Letters: %d\n", capital_letter_count);
    printf("Whitespaces: %d\n", whitespace_count);
    printf("Newlines: %d\n", newline_count);
    printf("Tabs: %d\n", tab_count);

    return 0;
}
