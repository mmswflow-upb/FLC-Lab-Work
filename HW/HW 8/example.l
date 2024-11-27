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
 
 
[\n] {
 printf("Hello World\n"); 
}
 
 
%%
 
 
int main()
{
 yylex(); //calling the rules section
}