%option noyywrap

%{
#include <stdio.h>
#include <math.h>

#define YY_DECL int yylex()

#include "Ex15_Sakka_MohamadMario.tab.h"

int expect_unary = 1;

%}

%%

[ \t]                ; 
[0-9]+\.[0-9]+       { 
                        yylval.fval = atof(yytext); 
                        expect_unary = 0; 
                        return T_FLOAT; 
                     } 
[0-9]+               { 
                        yylval.fval = atof(yytext); 
                        expect_unary = 0; 
                        return T_FLOAT; 
                     } 
"-"                  { 
                        if (expect_unary) {
                            expect_unary = 1; 
                            return T_MINUS; 
                        } else {
                            expect_unary = 1; 
                            return T_MINUS; 
                        }
                     }
\n                   { expect_unary = 1; return T_NEWLINE; }
"+"                  { expect_unary = 1; return T_PLUS; }
"*"                  { expect_unary = 1; return T_MULT; }
"/"                  { expect_unary = 1; return T_DIV; }
"^"                  { expect_unary = 1; return T_POW; }    
"("                  { expect_unary = 1; return T_LPAREN; } 
")"                  { expect_unary = 0; return T_RPAREN; } 
.                    { printf("Unrecognized input: %s\n", yytext); } // Handle invalid input
%%
