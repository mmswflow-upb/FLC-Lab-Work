%{
#include <stdio.h>
#undef yywrap
#define yywrap() 1
%}

%%
[a-zA-Z0-9._%+-]+@([a-zA-Z0-9_-]+\.)+[a-zA-Z]{2,} { 
    printf("Valid Email with Subdomains: %s\n", yytext); 
}

[a-zA-Z0-9._%+-]*@[a-zA-Z0-9_-]* { 
    printf("Invalid Email: %s (incomplete domain)\n", yytext); 
}

.* {
    printf("Invalid Input: %s\n", yytext);
}

\n   {  }

%%

int main(void) {
    printf("Enter strings to validate email addresses (Ctrl+D to stop):\n");
    yylex(); 
    return 0;
}
