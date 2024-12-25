%option noyywrap

%{
#include <stdio.h>
#include <math.h>

#define YY_DECL int yylex()

#include "Ex15_Sakka_MohamadMario.tab.h"

%}

%%

[ \t]                ;
[0-9]+"."[0-9]+      { yylval.fval = atof(yytext); return T_FLOAT; } 
[0-9]+               { yylval.fval = atof(yytext); return T_FLOAT; } 
\n                   { return T_NEWLINE; }
"+"                  { return T_PLUS; }
"-"                  { return T_MINUS; }
"*"                  { return T_MULT; }
"/"                  { return T_DIV; }
"^"                  { return T_POW; }   
"("                  { return T_LPAREN; }
")"                  { return T_RPAREN; } 
%%