%{
#include <ctype.h>  
#undef yywrap
#define yywrap() 1

#define YY_INPUT(buf, result, max_size)  \
    { \
        int c = getchar(); \
        result = (c == EOF) ? YY_NULL : (buf[0] = tolower(c), 1); \
    }
 
%}
%%
(he|she|it|they|we|you|i|me|us|him|her)                     printf("Pronoun: %s\n", yytext);
(run|eat|sleep|walk|play|read|write|jump|swim|watch)        printf("Verb: %s\n", yytext);
(happy|sad|tall|short|big|small|fast|slow|bright|dark)      printf("Adjective: %s\n", yytext);
(dog|cat|car|house|book|tree|sky|child|computer|teacher)    printf("Noun: %s\n", yytext);
(in|on|at|under|over|with|by|about|against|between)         printf("Preposition: %s\n", yytext);
[0-9]+                                                     printf("Digit: %s\n", yytext);
[a-zA-Z]+                                                  printf("Not recognized: %s\n", yytext);
%%
int main(void) {
    yylex();  // Run the lexer
    return 0;
}
