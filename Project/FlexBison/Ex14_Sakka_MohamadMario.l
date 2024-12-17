%{
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

float result = 0.0;  // Stores the result of calculations
int operation_done = 0; // Flag to check if calculation has occurred

void calculate(float num1, char op, float num2);
%}

%option noyywrap

%%

[0-9]*\.[0-9]+|[0-9]+(\.[0-9]*)? {
    result = atof(yytext); // Convert the matched float number
    operation_done = 1;
}

\+|\/|\*|\- {
    char op = yytext[0]; // Capture operator
    float num;
    scanf("%f", &num);   // Read the next number
    calculate(result, op, num);
}

sqrt[ \t]*\([0-9]*\.[0-9]+|[0-9]+(\.[0-9]*)?\) {
    float num;
    sscanf(yytext, "sqrt(%f)", &num);
    if (num < 0) {
        printf("Error: Cannot calculate square root of a negative number.\n");
    } else {
        result = sqrt(num);
        operation_done = 1;
    }
}

\n {
    if (operation_done) {
        printf("Result: %.2f\n", result);
        result = 0.0; // Reset result for new input
        operation_done = 0; // Reset flag
    }
}

[ \t]+ { /* Ignore whitespace */ }

. {
    printf("Invalid input: %s\n", yytext);
}

%%

void calculate(float num1, char op, float num2) {
    switch (op) {
        case '+': result = num1 + num2; break;
        case '-': result = num1 - num2; break;
        case '*': result = num1 * num2; break;
        case '/':
            if (num2 == 0) {
                printf("Error: Division by zero is not allowed.\n");
                result = 0.0;
                return;
            }
            result = num1 / num2; break;
    }
    operation_done = 1;
}

int main(void) {
    printf("Enter calculations (e.g., 3.2 + 2.1, sqrt(16)):\n");
    yylex(); // Start the lexer
    return 0;
}
