%{
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

extern int yylex();
extern int yyparse();
extern FILE* yyin;

void yyerror(const char* s);

double factorial(double n);
%}

%union {
    float fval;
}

%token<fval> T_FLOAT
%token T_PLUS T_MINUS T_MULT T_DIV T_POW T_LPAREN T_RPAREN T_NEWLINE
%token T_FACTORIAL T_SIN T_COS T_SQRT T_FABS T_SINH T_COSH


%left T_PLUS T_MINUS
%left T_MULT T_DIV
%right T_POW
%nonassoc T_FACTORIAL 
%nonassoc T_LPAREN T_RPAREN

%type<fval> expression

%start calculation

%%

calculation:
      | calculation line
;

line:
      T_NEWLINE
    | expression T_NEWLINE { printf("\tResult: %.6f\n", $1); }
;

expression:
      T_FLOAT                      { $$ = $1; }
    | expression T_PLUS expression { $$ = $1 + $3; }
    | expression T_MINUS expression { $$ = $1 - $3; }
    | expression T_MULT expression { $$ = $1 * $3; }
    | expression T_DIV expression {
          if ($3 == 0.0) {
              yyerror("Division by zero");
          } else {
              $$ = $1 / $3;
          }
      }
    | expression T_POW expression { $$ = pow($1, $3); }
    | T_LPAREN expression T_RPAREN { $$ = $2; }
    | expression T_FACTORIAL {
          if ($1 < 0 || (int)$1 != $1) {
              yyerror("Factorial is only defined for non-negative integers.");
          } else {
              $$ = factorial($1);
          }
      }
    | T_SIN T_LPAREN expression T_RPAREN { $$ = sin($3); }
    | T_COS T_LPAREN expression T_RPAREN { $$ = cos($3); }
    | T_SQRT T_LPAREN expression T_RPAREN {
          if ($3 < 0) {
              yyerror("Square root of negative number is not allowed.");
          } else {
              $$ = sqrt($3);
          }
      }
    | T_FABS T_LPAREN expression T_RPAREN { $$ = fabs($3); }
    | T_SINH T_LPAREN expression T_RPAREN { $$ = sinh($3); }
    | T_COSH T_LPAREN expression T_RPAREN { $$ = cosh($3); }
;

%%

double factorial(double n) {
    if (n == 0) return 1;
    double result = 1.0;
    for (int i = 1; i <= (int)n; ++i) {
        result *= i;
    }
    return result;
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
