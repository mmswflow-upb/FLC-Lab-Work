%{
#include<stdio.h>
#include<string.h>

char oldWord[] = "bruh"; 
char newWord[] = "why so serious?"; // Replacement word
%}

%%
[a-zA-Z]+ {
    if (strcmp(yytext, oldWord) == 0) {
        fprintf(yyout, "%s", newWord); 
    } else {
        fprintf(yyout, "%s", yytext); 
    }
}
[ \t\n] { 
    fprintf(yyout, "%s", yytext); 
}
.       { 
    fprintf(yyout, "%s", yytext); 
}
%%

int yywrap() {
    return 1; 
}

int main() {
    extern FILE *yyin, *yyout;

    yyin = fopen("in", "r"); 
    yyout = fopen("out", "w"); 

    if (!yyin || !yyout) {
        perror("Error opening files");
        return 1;
    }

    yylex(); 

    fclose(yyin); 
    fclose(yyout); 

    printf("Check the out file.\n");
    return 0;
}