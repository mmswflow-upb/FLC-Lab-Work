%{
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

float result = 0.0;       
char pending_op = 0;      
int operation_done = 0;   

void apply_operator(float num);
%}

%option noyywrap

%%

[0-9]*\.[0-9]+|[0-9]+(\.[0-9]*)? {
    float num = atof(yytext);  
    if (pending_op) {
        apply_operator(num);  
    } else {
        result = num;         
    }
    operation_done = 1;
}

[\+\-x\/] {
    pending_op = yytext[0];    
    if (pending_op == 'x') pending_op = '*';
}

sqrt[ \t]*\(([0-9]*\.[0-9]+|[0-9]+(\.[0-9]*)?)\) {
    float num;
    if (sscanf(yytext, "sqrt(%f)", &num) == 1) {
        if (num < 0) {
            printf("Error: Cannot calculate square root of a negative number.\n");
        } else {
            result = sqrt(num);
            pending_op = 0; 
            operation_done = 1;
        }
    } else {
        printf("Error: Invalid sqrt syntax.\n");
    }
}

\n {
    if (operation_done) {
        printf("Result: %.2f\n", result);
        result = 0.0;        
        pending_op = 0;      
        operation_done = 0;  
    }
}

[ \t]+ {  }

. {
    printf("Invalid input: %s\n", yytext);
}

%%

void apply_operator(float num) {
    switch (pending_op) {
        case '+': result += num; break;
        case '-': result -= num; break;
        case '*': result *= num; break;
        case '/':
            if (num == 0) {
                printf("Error: Division by zero is not allowed.\n");
                result = 0.0;
            } else {
                result /= num;
            }
            break;
        default:
            printf("Error: Unknown operator '%c'.\n", pending_op);
    }
    pending_op = 0;  
}

int main(void) {
    printf("Enter calculations (e.g., 3.0 + 5.0 - 1.0, sqrt(16)):\n");
    yylex(); 
    return 0;
}
