%{
#include <stdio.h>

int capital_word_count = 0;  

#undef yywrap
#define yywrap() 1
%}

%%

[A-Z][a-zA-Z]* { 
    capital_word_count++;  
}

[a-zA-Z]+ { 
  
}

[ \t\n]+ { 
}

. { 
}

%%

int main(void) {
    printf("Enter text (Ctrl+D to stop):\n");
    yylex(); 
    
    printf("\nNumber of words starting with a capital letter: %d\n", capital_word_count);
    return 0;
}
