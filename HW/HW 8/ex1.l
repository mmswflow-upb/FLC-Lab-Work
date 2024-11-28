%{
#undef yywrap
#define yywrap() 1
  #define YY_INPUT(buf,result,max_size) \
	       { \
	       int c = getchar(); \
	       result = (c == EOF) ? YY_NULL : (buf[0] = c, 1); \
	       }
 
%}
%%
[aeiouAEIOU]    printf("Vowel: %s\n", yytext);
.               printf("Not a vowel: %s\n", yytext);
%%
int main(void) {
    yylex();  // Run the lexer
    return 0;
}
