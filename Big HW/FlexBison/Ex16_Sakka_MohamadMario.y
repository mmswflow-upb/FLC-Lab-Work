// Definitions Section
%{
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

extern int yylex();
extern int yyparse();
extern FILE* yyin;

void yyerror(const char* s);
float factorial(float n); // Function prototype for factorial
%}

// Rules Section
%union {
    float fval; // Use float for calculations
}

%token<fval> T_FLOAT
%token T_PLUS T_MINUS T_MULT T_DIV T_POW T_FACTORIAL T_LPAREN T_RPAREN
%token T_SIN T_COS T_SQRT T_FABS T_SINH T_COSH
%token T_NEWLINE


%left T_PLUS T_MINUS
%left T_MULT T_DIV
%right T_POW        
%right T_FACTORIAL  
%nonassoc T_LPAREN T_RPAREN

%type<fval> expression

%start calculation

%%

calculation:
      | calculation line
;

line:
      T_NEWLINE
    | expression T_NEWLINE { printf("\tResult: %.5f\n", $1); }
;

expression:
      T_FLOAT                      { $$ = $1; }
    | T_MINUS expression %prec T_FACTORIAL { $$ = -$2; }
    | expression T_PLUS expression { $$ = $1 + $3; }
    | expression T_MINUS expression { $$ = $1 - $3; }
    | expression T_MULT expression { $$ = $1 * $3; }
    | expression T_DIV expression {
          if ($3 == 0) {
              yyerror("Division by zero");
          } else {
              $$ = $1 / $3;
          }
      }
    | expression T_POW expression { $$ = pow($1, $3); } 
    | expression T_FACTORIAL {
          if ($1 < 0 || (int)$1 != $1) {
              yyerror("Factorial is not defined for negative or floats");
          } else {
              $$ = factorial($1);
          }
      }
    | T_SIN T_LPAREN expression T_RPAREN { $$ = sin($3); }
    | T_COS T_LPAREN expression T_RPAREN { $$ = cos($3); }
    | T_SQRT T_LPAREN expression T_RPAREN {
          if ($3 < 0) {
              yyerror("Square root is not defined for negative numbers");
          } else {
              $$ = sqrt($3);
          }
      }
    | T_FABS T_LPAREN expression T_RPAREN { $$ = fabs($3); } 
    | T_SINH T_LPAREN expression T_RPAREN { $$ = sinh($3); }
    | T_COSH T_LPAREN expression T_RPAREN { $$ = cosh($3); }
    | T_LPAREN expression T_RPAREN { $$ = $2; }
;

%%

float factorial(float n) {
    if (n == 0 || n == 1) return 1;
    return n * factorial(n - 1);
}

int main() {
    yyin = stdin;

    do {
        yyparse();
    } while (!feof(yyin));

    return 0;
}

void yyerror(const char* s) {
    fprintf(stderr, "Parse error: %s\n", s);
    exit(1);
}