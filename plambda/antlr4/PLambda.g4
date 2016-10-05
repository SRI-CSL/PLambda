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
          |  '(' N_ARY_OP expression* ')'                                                # naryExpression       
          |  '(' TRY expression+  catchExpression ')'                                    # tryExpression		
          |  '(' FOR ID rangeExpression expression+ ')'                                  # forExpression
          |  STRING                                                                      # stringLiteral
          |  ID                                                                          # identifierLiteral
          |  NONE                                                                        # noneLiteral
           ;

parameterList: '(' parameter* ')' ;

parameter: ID ;

bindingList: '(' bindingPair+ ')' ;

bindingPair: '(' parameter   expression ')' ;

catchExpression:  '(' CATCH  parameter expression+  ')' ;

rangeExpression: expression ;

data: ID     |     
      NUMBER   
      ;  

token : ID        |
        STRING
    ;

STRING :
       STRING_DQ |
       STRING_SQ 
       ;

PRIMITIVE_DATA_OP:  
                    INT      |
		    FLOAT    | 
		    BOOLEAN
                    ;
       
UNARY_OP :   FETCH      |
	     GETUID     |
             GLOBAL     |
             IMPORT     |
             ISNONE     |
             ISOBJECT   |
             ISINT      |
             ISFLOAT    |
	     LOAD       |
	     NOT        |
	     THROW
             ;

BINARY_OP :  '+'           |
             '*'           |
             '/'           |
             '%'           |
             '<'           |
             '>'           |
             '<='          |
             '>='          |
             IS            |
             '=='          |
             '!='          |
	     GET           |
	     SETUID        |
             LOOKUP  	     
	     ;
	     
TERNARY_OP : KWAPPLY   |
	     MODIFY    |
	     UPDATE    |
             SUPDATE   |
             SETATTR
             ;
        
N_ARY_OP :   CONCAT   |
             AND      |
             OR       |
	     MKTUPLE  |
	     MKLIST   |
	     MKDICT   
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

FOR:          [Ff][Oo][Rr]                              ;

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

ISINT:        [Ii][Ss][Ii][Nn][Tt]                      ;

ISFLOAT:      [Ii][Ss][Ff][Ll][Oo][Aa][Tt]              ;

GETUID:       [Gg][Ee][Tt][Uu][Ii][Dd]                  ;
 
GLOBAL:       [Gg][Ll][Oo][Bb][Aa][Ll]                  ;
 
NOT:          [Nn][Oo][Tt]                              ;

THROW:        [Tt][Hh][Rr][Oo][Ww]                      ;

FETCH:        [Ff][Ee][Tt][Cc][Hh]                      ;

/* binary operators  */

NARROW:       [Nn][Aa][Rr][Rr][Oo][Ww]                  ;

INSTANCEOF:   [Ii][Nn][Ss][Tt][Aa][Nn][Cc][Ee][Oo][Ff]  ;

GET:          [Gg][Ee][Tt]                              ;

IS:           [Ii][Ss]                                  ;

LOOKUP:       [Ll][Oo][Oo][Kk][Uu][Pp]                  ;

SETUID:       [Ss][Ee][Tt][Uu][Ii][Dd]                  ;

/* ternary operators */

KWAPPLY:      [Kk][Ww][Aa][Pp][Pp][Ll][Yy]              ;

MODIFY:       [Mm][Oo][Dd][Ii][Ff][Yy]                  ;

UPDATE:       [Uu][Pp][Dd][Aa][Tt][Ee]                  ;

SUPDATE:      [Ss][Uu][Pp][Dd][Aa][Tt][Ee]              ;

SETATTR:      [Ss][Ee][Tt][Aa][Tt][Tt][Rr]              ;


/* n-nary operators */

CONCAT:       [Cc][Oo][Nn][Cc][Aa][Tt]                  ;

AND:          [Aa][Nn][Dd]                              ;

OR:           [Oo][Rr]                                  ;

MKTUPLE:      [Mm][Kk][Tt][Uu][Pp][Ll][Ee]              ;

MKLIST:       [Mm][Kk][Ll][Ii][Ss][Tt]                  ;

MKDICT:       [Mm][Kk][Dd][Ii][Cc][Tt]                  ;

/* one or more operators */

MINUS:        '-'                                       ;
 
/* two or more operators */

IF:           [Ii][Ff]                                  ;

GETATTR:      [Gg][Ee][Tt][Aa][Tt][Tt][Rr]              ;

ID  :   (SYMBOL | LETTER | DIGIT) (LETTER | DIGIT | SYMBOL)*;

NUMBER      :   '-'? ('.' DIGIT+ | DIGIT+ ('.' DIGIT*)? ) ;

fragment
DIGIT       :   [0-9] ;


/* need to define Single Quoted String: STRING_SQ and Double Quoted String: STRING_DQ */
STRING_SQ   :   '\'' (ESCAPE_SQ|.)*? '\'' ;
fragment 
ESCAPE_SQ   :   '\\\'' | '\\\\'  ;

STRING_DQ      :   '"' (ESCAPE_DQ|.)*? '"' ;
fragment 
ESCAPE_DQ      :   '\\"' | '\\\\'  ;



fragment
LETTER      :   [a-zA-Z\u0080-\u00FF_] ;

/* note that we are more generous than Java here      v ... new as of 8/5/2015 mainly for the (QUOTE string) clause */
SYMBOL: '$' | '?' | '.' | '_' | '-' | '[' | ']' | ';' | '/' | '*' | '@' | '#' | '&' | '!' | '~' | '^' | '{' | '}' | '|' | ':';

LINE_COMMENT : ';' .*? '\r'? '\n'  -> skip ;

NEW_LINE_COMMENT : '//' .*? '\r'?  '\n' -> skip ;

NEW_COMMENT : '/*' .*? '*/' -> skip ;

WHITE_SPACE: [ \t\r\n]+ -> skip ;
