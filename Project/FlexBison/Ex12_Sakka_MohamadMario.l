%{
#include <stdio.h>

int capital_word_count = 0;  // Counter for words starting with a capital letter

#undef yywrap
#define yywrap() 1
%}

%%

[A-Z][a-zA-Z]* { 
    capital_word_count++;  // Increment the counter for words starting with a capital letter
}

[a-zA-Z]+ { 
    /* Matches other words but takes no action */
}

[ \t\n]+ { 
    /* Matches whitespace (spaces, tabs, newlines) and skips it */
}

. { 
    /* Matches any other character and skips it */
}

%%

int main(void) {
    printf("Enter text (Ctrl+D to stop):\n");
    yylex(); // Start the lexer
    
    printf("\nNumber of words starting with a capital letter: %d\n", capital_word_count);
    return 0;
}
