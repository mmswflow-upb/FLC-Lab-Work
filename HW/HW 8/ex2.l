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

he|she|it|they|we|you|i|me|us|him|her {
    printf("Pronoun: %s\n", yytext);
}

[a-zA-Z]+ {
    printf("Not a pronoun: %s\n", yytext);
}

%%

int main(void) {
    yylex();  
    return 0;
}
