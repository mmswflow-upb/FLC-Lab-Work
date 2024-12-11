// Definitions Section
%{
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

extern int yylex();
extern int yyparse();
extern FILE* yyin;

void yyerror(const char* s);
%}

// Rules Section
%union {
    int ival;
}

%token<ival> T_INT
%token T_PLUS T_MINUS T_MULT T_DIV T_POW T_LPAREN T_RPAREN
%token T_NEWLINE

// Define operator precedence and associativity
%left T_PLUS T_MINUS
%left T_MULT T_DIV
%right T_POW        // Exponentiation has higher precedence and right associativity
%nonassoc T_LPAREN T_RPAREN

%type<ival> expression

%start calculation

%%

calculation:
      | calculation line
;

line:
      T_NEWLINE
    | expression T_NEWLINE { printf("\tResult: %i\n", $1); }
;

expression:
      T_INT                      { $$ = $1; }
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
    | expression T_POW expression { $$ = pow($1, $3); } // Exponentiation
    | T_LPAREN expression T_RPAREN { $$ = $2; } // Parentheses
;

%%

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
