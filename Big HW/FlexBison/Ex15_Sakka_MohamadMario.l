%option noyywrap

%{
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define YY_DECL int yylex()

#include "Ex15_Sakka_MohamadMario.tab.h"

%}

%%

[ \t]                ; // Ignore whitespace
[0-9]+\.[0-9]+       { yylval.fval = atof(yytext); return T_FLOAT; } // Match floats
[0-9]+               { yylval.fval = atof(yytext); return T_FLOAT; } // Match integers as floats
\n                   { return T_NEWLINE; }
"+"                  { return T_PLUS; }
"-"                  { return T_MINUS; }
"*"                  { return T_MULT; }
"/"                  { return T_DIV; }
"^"                  { return T_POW; }    // Exponentiation
"("                  { return T_LPAREN; } // Left parenthesis
")"                  { return T_RPAREN; } // Right parenthesis

.                    { printf("Unknown character: %s\n", yytext); }
