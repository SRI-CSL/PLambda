grammar PLambda;


unit : expression+ ;


expression:  '(' SEQ expression+ ')'                                                     # seqExpression
          |  '(' LET binding_list expression+ ')'                                        # letExpression           
          |  '(' DEFINE ID parameter_list? expression+ ')'                               # defineExpression         
          |  '(' LAMBDA parameter_list expression+ ')'                                   # lambdaExpression         
          |  '(' INVOKE  expression expression expression* ')'                           # invokeExpression         
          |  '(' APPLY expression expression* ')'                                        # applyExpression          
          |  '(' PRIMITIVE_DATA_OP data ')'                                              # dataExpression 
          |  '(' UNARY_OP expression ')'                                                 # unaryExpression       
          |  '(' BINARY_OP expression expression ')'                                     # binaryExpression      
          |  '(' TERNARY_OP expression expression expression ')'                         # ternaryExpression     
          |  '(' QUOTE  string ')'                                                       # quoteExpression             
          |  STRING                                                                      # stringLiteral      
          |  ID                                                                          # identifierLiteral
           ;

parameter_list: '(' parameter* ')' ;

parameter: ID ;

binding_list: '(' binding_pair+ ')' ;

binding_pair: '(' parameter   expression ')' ;

catch_expression:  '(' CATCH  parameter expression+  ')' ;

range_expression: expression ;

data: ID     |     
      NUMBER | 
      CHARACTER
      ;     

string: ID     |     
      NUMBER   
      ;  


token : ID        |
        STRING
    ;

type_expression: PRIMITIVE_DATA_OP | 
                 ID
                 ;

PRIMITIVE_DATA_OP:  
                    INT      |
		    BOOLEAN
                    ;
       
             

UNARY_OP :   LOAD       |
             ISNULL     |
             ISOBJECT   |
             QUOTE      |
             NOT        
             ;

BINARY_OP :  '+'           |
             '*'           |
             '/'           |
             '%'           |
             '<'           |
             '>'           |
             '<='          |
             '>='          |
             '='           |
             '=='          |
             '!='          
             ;

TERNARY_OP : UPDATE    |
             SUPDATE   |
             SETATTR
             ;
        
N_ARY_OP :   CONCAT   |
             AND      |
             OR  
             ;    

AMBI1_OP :   MINUS  
             ;    

AMBI2_OP :   IF       |
             GETATTR  
             ;    

/* null is **not** case insensitive */

NULL:         'null' ;

SEQ:          [Ss][Ee][Qq]                              ;

DO:           [Dd][Oo]                                  ;

LET:          [Ll][Ee][Tt]                              ;

DEFINE:       [Dd][Ee][Ff][Ii][Nn][Ee]                  ;

LAMBDA:       [Ll][Aa][Mm][Bb][Dd][Aa]                  ;

APPLY:        [Aa][Pp][Pp][Ll][Yy]                      ;

INVOKE:       [Ii][Nn][Vv][Oo][Kk][Ee]                  ;

SINVOKE:      [Ss][Ii][Nn][Vv][Oo][Kk][Ee]              ;

OBJECT:       [Oo][Bb][Jj][Ee][Cc][Tt]                  ;

FOR:          [Ff][Oo][Rr]                              ;

ARRAY:        [Aa][Rr][Rr][Aa][Yy]                      ;

MKARRAY:      [Mm][Kk][Aa][Rr][Rr][Aa][Yy]              ;

TRY:          [Tt][Rr][Yy]                              ;

CATCH:        [Cc][Aa][Tt][Cc][Hh]                      ;

/* primitive data  */

BOOLEAN:      [Bb][Oo][Oo][Ll][Ee][Aa][Nn]              ;

BYTE:         [Bb][Yy][Tt][Ee]                          ;

DOUBLE:       [Dd][Oo][Uu][Bb][Ll][Ee]                  ;

CHAR:         [Cc][Hh][Aa][Rr]                          ;

FLOAT:        [Ff][Ll][Oo][Aa][Tt]                      ;

INT:          [Ii][Nn][Tt]                              ;

LONG:         [Ll][Oo][Nn][Gg]                          ;

SHORT:        [Ss][Hh][Oo][Rr][Tt]                      ;

/* unary operators */

LOAD:         [Ll][Oo][Aa][Dd]                          ;

ISNULL:       [Ii][Ss][Nn][Uu][Ll][Ll]                  ;

ISOBJECT:     [Ii][Ss][Oo][Bb][Jj][Ee][Cc][Tt]          ;

GETUID:       [Gg][Ee][Tt][Uu][Ii][Dd]                  ;
 
QUOTE:        [Qq][Uu][Oo][Tt][Ee]                      ;

NOT:          [Nn][Oo][Tt]                              ;

THROW:        [Tt][Hh][Rr][Oo][Ww]                      ;

FETCH:        [Ff][Ee][Tt][Cc][Hh]                      ;

/* binary operators  */

NARROW:       [Nn][Aa][Rr][Rr][Oo][Ww]                  ;

INSTANCEOF:   [Ii][Nn][Ss][Tt][Aa][Nn][Cc][Ee][Oo][Ff]  ;

AGET:         [Aa][Gg][Ee][Tt]                          ;

LOOKUP:       [Ll][Oo][Oo][Kk][Uu][Pp]                  ;

SETUID:       [Ss][Ee][Tt][Uu][Ii][Dd]                  ;

/* ternary operators */

ASET:         [Aa][Ss][Ee][Tt]                          ;

UPDATE:       [Uu][Pp][Dd][Aa][Tt][Ee]                  ;

SUPDATE:      [Ss][Uu][Pp][Dd][Aa][Tt][Ee]              ;

SETATTR:      [Ss][Ee][Tt][Aa][Tt][Tt][Rr]              ;


/* n-nary operators */

CONCAT:       [Cc][Oo][Nn][Cc][Aa][Tt]                  ;

AND:          [Aa][Nn][Dd]                              ;

OR:           [Oo][Rr]                                  ;

/* one or more operators */

MINUS:        '-'                                       ;
 
/* two or more operators */

IF:           [Ii][Ff]                                  ;

GETATTR:      [Gg][Ee][Tt][Aa][Tt][Tt][Rr]              ;

CHARACTER : '\'' (. | '\\' ID ) '\'';

ID  :   (SYMBOL | LETTER | DIGIT) (LETTER | DIGIT | SYMBOL)*;

NUMBER      :   '-'? ('.' DIGIT+ | DIGIT+ ('.' DIGIT*)? ) ;

fragment
DIGIT       :   [0-9] ;

STRING      :   '"' (ESCAPE|.)*? '"' ;
fragment 
ESCAPE      :   '\\"' | '\\\\'  ;


fragment
LETTER      :   [a-zA-Z\u0080-\u00FF_] ;

/* note that we are more generous than Java here      v ... new as of 8/5/2015 mainly for the (QUOTE string) clause */
SYMBOL: '$' | '?' | '.' | '_' | '-' | '[' | ']' | ';' | '/' | '*' | '@' | '#' | '&' | '!' | '~' | '^' | '{' | '}' | '|' | ':';

LINE_COMMENT : ';' .*? '\r'? '\n'  -> skip ;

NEW_LINE_COMMENT : '//' .*? '\r'?  '\n' -> skip ;

NEW_COMMENT : '/*' .*? '*/' -> skip ;

WHITE_SPACE: [ \t\r\n]+ -> skip ;
