%{
#include "Ex17_Sakka_MohamadMario.tab.h"
#include <stdlib.h>  

int binary_to_decimal(const char* binary); 
%}

%%

[01]+              { yylval.ival = binary_to_decimal(yytext); return T_BINARY; }
"+"                { return T_PLUS; }
"-"                { return T_MINUS; }
"*"                { return T_MULT; }
"/"                { return T_DIV; }
\n                 { return T_NEWLINE; }
[ \t]+             ; 
.                  { printf("Unknown character: %s\n", yytext); }

%%

int yywrap() {
    return 1;
}
