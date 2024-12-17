%{
#include <ctype.h>  
#include <stdio.h>

#undef yywrap
#define yywrap() 1

#define YY_INPUT(buf, result, max_size)  \
    { \
        int c = getchar(); \
        result = (c == EOF) ? YY_NULL : (buf[0] = tolower(c), 1); \
    }

int pronoun_count = 0, verb_count = 0, adjective_count = 0;
int noun_count = 0, preposition_count = 0, digit_count = 0, not_recognized_count = 0;

%}
%%

(he|she|it|they|we|you|i|me|us|him|her) { 
    printf("Pronoun: %s\n", yytext); 
    pronoun_count++; 
}

(run|eat|sleep|walk|play|read|write|jump|swim|watch|met|going|doing|ing) { 
    printf("Verb: %s\n", yytext); 
    verb_count++; 
}

(happy|sad|tall|short|big|small|fast|slow|bright|dark) { 
    printf("Adjective: %s\n", yytext); 
    adjective_count++; 
}

(dog|cat|car|house|book|tree|sky|child|computer|teacher) { 
    printf("Noun: %s\n", yytext); 
    noun_count++; 
}

(in|on|at|under|over|with|by|about|against|between) { 
    printf("Preposition: %s\n", yytext); 
    preposition_count++; 
}

[0-9]+ { 
    printf("Digit: %s\n", yytext); 
    digit_count++; 
}

[a-zA-Z]+ { 
    printf("Not recognized: %s\n", yytext); 
    not_recognized_count++; 
}

%%

int main(void) {
    printf("Enter text (Ctrl+D to stop):\n");
    yylex();  

    printf("\nCounts Summary:\n");
    printf("Pronouns: %d\n", pronoun_count);
    printf("Verbs: %d\n", verb_count);
    printf("Adjectives: %d\n", adjective_count);
    printf("Nouns: %d\n", noun_count);
    printf("Prepositions: %d\n", preposition_count);
    printf("Digits: %d\n", digit_count);
    printf("Not recognized: %d\n", not_recognized_count);

    return 0;
}
