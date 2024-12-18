%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

extern int yylex();
void yyerror(const char* s);

int binary_to_decimal(const char* binary);
char* decimal_to_binary(int decimal);
%}

%union {
    int ival;  
}

%token<ival> T_BINARY
%token T_PLUS T_MINUS T_MULT T_DIV T_NEWLINE
%type<ival> expression

%left T_PLUS T_MINUS
%left T_MULT T_DIV

%start calculation

%%

calculation:
    | calculation line
;

line:
    expression T_NEWLINE {
        char* result_binary = decimal_to_binary($1);
        printf("Result: %s\n", result_binary);
        free(result_binary);
    }
;

expression:
      T_BINARY                  { $$ = $1; }
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
;

%%

int binary_to_decimal(const char* binary) {
    int decimal = 0;
    while (*binary) {
        decimal = decimal * 2 + (*binary - '0');
        binary++;
    }
    return decimal;
}

char* decimal_to_binary(int decimal) {
    if (decimal == 0) {
        char* result = malloc(2);
        strcpy(result, "0");
        return result;
    }

    char buffer[65]; 
    buffer[64] = '\0';
    int index = 63;

    while (decimal > 0) {
        buffer[index--] = (decimal % 2) + '0';
        decimal /= 2;
    }

    char* result = strdup(&buffer[index + 1]);
    return result;
}

void yyerror(const char* s) {
    fprintf(stderr, "Error: %s\n", s);
    exit(1);
}

int main() {
    printf("Enter binary calculations (e.g., 1010 + 110):\n");
    return yyparse();
}
