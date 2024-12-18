%option noyywrap

%{
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define YY_DECL int yylex()

#include "Ex16_Sakka_MohamadMario.tab.h"

%}

%%

[ \t]                ; 
[0-9]+\.[0-9]+       { yylval.fval = atof(yytext); return T_FLOAT; }
[0-9]+               { yylval.fval = atof(yytext); return T_FLOAT; } 
"!"                  { return T_FACTORIAL; }
"sin"                { return T_SIN; }
"cos"                { return T_COS; }
"sqrt"               { return T_SQRT; }
"fabs"               { return T_FABS; }
"sinh"               { return T_SINH; }
"cosh"               { return T_COSH; }
\n                   { return T_NEWLINE; }
"+"                  { return T_PLUS; }
"-"                  { return T_MINUS; }
"x"                  { return T_MULT; }
"/"                  { return T_DIV; }
"^"                  { return T_POW; }
"("                  { return T_LPAREN; }
")"                  { return T_RPAREN; }

.                    { printf("Unknown character: %s\n", yytext); }
