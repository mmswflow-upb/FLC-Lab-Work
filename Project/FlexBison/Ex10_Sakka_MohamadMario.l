%{
#include <stdio.h>
#include <ctype.h>

#undef yywrap
#define yywrap() 1

%}

%%
[0-9]+      { printf("Number: %s\n", yytext); }
[a-zA-Z]+   { printf("Word: %s\n", yytext); }
.           { printf("Other: %s\n", yytext); }
\n          { /* Ignore newlines */ }

%%

int main(void) {
    printf("Enter text (Ctrl+D to stop):\n");
    yylex();  
    return 0;
}
