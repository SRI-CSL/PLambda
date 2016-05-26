grammar PLambda;


unit : expression+ ;


expression:  '(' SEQ expression+ ')'                                                     # seqExpression
          |  '(' LET bindingList expression+ ')'                                         # letExpression           
          |  '(' DEFINE ID parameterList? expression+ ')'                                # defineExpression         
          |  '(' LAMBDA parameterList expression+ ')'                                    # lambdaExpression         
          |  '(' INVOKE  expression expression expression* ')'                           # invokeExpression         
          |  '(' APPLY expression expression* ')'                                        # applyExpression          
          |  '(' PRIMITIVE_DATA_OP data ')'                                              # dataExpression 
          |  '(' UNARY_OP expression ')'                                                 # unaryExpression       
          |  '(' BINARY_OP expression expression ')'                                     # binaryExpression      
          |  '(' TERNARY_OP expression expression expression ')'                         # ternaryExpression
          |  '(' AMBI1_OP expression expression? ')'                                     # oneOrMoreExpression       
          |  '(' AMBI2_OP expression expression  expression? ')'                         # twoOrMoreExpression       
          |  '(' N_ARY_OP expression+ ')'                                                # naryExpression       
          |  '(' TRY expression+  catchExpression ')'                                    # tryExpression		
          |  '(' FOR ID rangeExpression expression+ ')'                                  # forExpression
          |  '(' QUOTE  string ')'                                                       # quoteExpression             
          |  STRING                                                                      # stringLiteral      
          |  ID                                                                          # identifierLiteral
           ;

parameterList: '(' parameter* ')' ;

parameter: ID ;

bindingList: '(' bindingPair+ ')' ;

bindingPair: '(' parameter   expression ')' ;

catchExpression:  '(' CATCH  parameter expression+  ')' ;

rangeExpression: expression ;

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

PRIMITIVE_DATA_OP:  
                    INT      |
		    FLOAT    | 
		    BOOLEAN
                    ;
       
UNARY_OP :   LOAD       |
             IMPORT     |
             ISNONE     |
             ISOBJECT   |
             QUOTE      |
	     THROW      |
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

/* None is **not** case insensitive */

NONE:         'None' ;

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

FLOAT:        [Ff][Ll][Oo][Aa][Tt]                      ;

INT:          [Ii][Nn][Tt]                              ;

/* unary operators */

LOAD:         [Ll][Oo][Aa][Dd]                          ;

IMPORT:       [Ii][Mm][Pp][Oo][Rr][Tt]                  ;

ISNONE:       [Ii][Ss][Nn][Oo][Nn][Ee]                  ;

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
