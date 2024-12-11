%option noyywrap

%{
#include <stdio.h>
#include <math.h>

#define YY_DECL int yylex()

#include "calculator.tab.h"

%}

%%

[ \t]                ; // Ignore whitespace
[0-9]+               { yylval.ival = atoi(yytext); return T_INT; }
\n                   { return T_NEWLINE; }
"+"                  { return T_PLUS; }
"-"                  { return T_MINUS; }
"x"                  { return T_MULT; }
"/"                  { return T_DIV; }
"^"                  { return T_POW; }    // New token for exponentiation
"("                  { return T_LPAREN; } // New token for left parenthesis
")"                  { return T_RPAREN; } // New token for right parenthesis
%%

