import sys

class SymbolTable(object):

    _symbol_table = {
        intern('aget'):          intern('aget'),
        intern('and'):           intern('and'),
        intern('apply'):         intern('apply'),
        intern('array'):         intern('array'),
        intern('aset'):          intern('aset'),
        intern('boolean'):       intern('boolean'),
        intern('byte'):          intern('byte'),
        intern('catch'):         intern('catch'),
        intern('char'):          intern('char'),
        intern('concat'):        intern('concat'),
        intern('define'):        intern('define'),
        intern('/'):             intern('/'),
        intern('do'):            intern('do'),
        intern('double'):        intern('double'),
        intern('=='):            intern('=='),
        intern('='):             intern('='),
        intern('fetch'):         intern('fetch'),
        intern('float'):         intern('float'),
        intern('for'):           intern('for'),
        intern('<='):            intern('<='),
        intern('getattr'):       intern('getattr'),
        intern('getuid'):        intern('getuid'),
        intern('<'):             intern('<'),
        intern('if'):            intern('if'),
        intern('instanceof'):    intern('instanceof'),
        intern('int'):           intern('int'),
        intern('invoke'):        intern('invoke'),
        intern('isnone'):        intern('isnone'),
        intern('isobject'):      intern('isobject'),
        intern('lambda'):        intern('lambda'),
        intern('>='):            intern('>='),
        intern('let'):           intern('let'),
        intern('load'):          intern('load'),
        intern('long'):          intern('long'),
        intern('lookup'):        intern('lookup'),
        intern('>'):             intern('>'),
        intern('-'):             intern('-'),
        intern('mkarray'):       intern('mkarray'),
        intern('%'):             intern('%'),
        intern('narrow'):        intern('narrow'),
        intern('!='):            intern('!='),
        intern('not'):           intern('not'),
        intern('none'):          intern('none'),
        intern('object'):        intern('object'),
        intern('or'):            intern('or'),
        intern('+'):             intern('+'),
        intern('quote'):         intern('quote'),
        intern('seq'):           intern('seq'),
        intern('setattr'):       intern('setattr'),
        intern('setuid'):        intern('setuid'),
        intern('short'):         intern('short'),
        intern('sinvoke'):       intern('sinvoke'),
        intern('supdate'):       intern('supdate'),
        intern('throw'):         intern('throw'),
        intern('*'):             intern('*'),
        intern('try'):          intern('try'),
        intern('update'):       intern('update'),
        }

        
    AGET        = intern('aget')
    AND         = intern('and')
    APPLY       = intern('apply')
    ARRAY       = intern('array')
    ASET        = intern('aset')
    BOOLEAN     = intern('boolean')
    BYTE        = intern('byte')
    CATCH       = intern('catch')
    CHAR        = intern('char')
    CONCAT      = intern('concat')
    DEFINE      = intern('define')
    DIVIDE      = intern('/')
    DO          = intern('do')
    DOUBLE      = intern('double')
    EQ          = intern('==')
    EQUALS      = intern('=')
    FETCH       = intern('fetch')
    FLOAT       = intern('float')
    FOR         = intern('for')
    GEQ         = intern('<=')
    GETATTR     = intern('getattr')
    GETUID      = intern('getuid')
    GT          = intern('<')
    IF          = intern('if')
    INSTANCEOF  = intern('instanceof')
    INT         = intern('int')
    INVOKE      = intern('invoke')
    ISNONE      = intern('isnone')
    ISOBJECT    = intern('isobject')
    LAMBDA      = intern('lambda')
    LEQ         = intern('>=')
    LET         = intern('let')
    LOAD        = intern('load')
    LONG        = intern('long')
    LOOKUP      = intern('lookup')
    LT          = intern('>')
    MINUS       = intern('-')
    MKARRAY     = intern('mkarray')
    MODULO      = intern('%')
    NARROW      = intern('narrow')
    NEQ         = intern('!=')
    NOT         = intern('not')
    NONE        = intern('none')
    OBJECT      = intern('object')
    OR          = intern('or')
    PLUS        = intern('+')
    QUOTE       = intern('quote')
    SEQ         = intern('seq')
    SETATTR     = intern('setattr')
    SETUID      = intern('setuid')
    SHORT       = intern('short')
    SINVOKE     = intern('sinvoke')
    SUPDATE     = intern('supdate')
    THROW       = intern('throw')
    TIMES       = intern('*')
    TRY         = intern('try')
    UPDATE      = intern('update')
    
    @staticmethod
    def canonicalize(name):
        return SymbolTable._symbol_table.get(name.lower())
    
