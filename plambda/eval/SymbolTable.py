import sys

class SymbolTable(object):

    _symbol_table = {
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
        intern('is'):            intern('is'),
        intern('fetch'):         intern('fetch'),
        intern('float'):         intern('float'),
        intern('for'):           intern('for'),
        intern('<='):            intern('<='),
        intern('get'):           intern('get'),
        intern('getattr'):       intern('getattr'),
        intern('getuid'):        intern('getuid'),
        intern('global'):        intern('global'),
        intern('<'):             intern('<'),
        intern('if'):            intern('if'),
        intern('import'):        intern('import'),
        intern('instanceof'):    intern('instanceof'),
        intern('int'):           intern('int'),
        intern('invoke'):        intern('invoke'),
        intern('isnone'):        intern('isnone'),
        intern('isfloat'):       intern('isfloat'),
        intern('isint'):         intern('isint'),
        intern('isobject'):      intern('isobject'),
        intern('kwapply'):       intern('kwapply'),
        intern('lambda'):        intern('lambda'),
        intern('>='):            intern('>='),
        intern('let'):           intern('let'),
        intern('load'):          intern('load'),
        intern('long'):          intern('long'),
        intern('lookup'):        intern('lookup'),
        intern('>'):             intern('>'),
        intern('-'):             intern('-'),
        intern('mktuple'):       intern('mktuple'),
        intern('mklist'):        intern('mklist'),
        intern('mkdict'):        intern('mkdict'),
        intern('modify'):        intern('modify'),
        intern('%'):             intern('%'),
        intern('narrow'):        intern('narrow'),
        intern('!='):            intern('!='),
        intern('not'):           intern('not'),
        intern('none'):          intern('none'),
        intern('object'):        intern('object'),
        intern('or'):            intern('or'),
        intern('+'):             intern('+'),
        intern('seq'):           intern('seq'),
        intern('setattr'):       intern('setattr'),
        intern('setuid'):        intern('setuid'),
        intern('short'):         intern('short'),
        intern('sinvoke'):       intern('sinvoke'),
        intern('supdate'):       intern('supdate'),
        intern('throw'):         intern('throw'),
        intern('*'):             intern('*'),
        intern('try'):           intern('try'),
        intern('update'):        intern('update'),
        }

        
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
    IS          = intern('is')
    EQUALS      = intern('==')
    FETCH       = intern('fetch')
    FLOAT       = intern('float')
    FOR         = intern('for')
    GEQ         = intern('<=')
    GET         = intern('get')
    GETATTR     = intern('getattr')
    GETUID      = intern('getuid')
    GLOBAL      = intern('global')
    GT          = intern('<')
    IF          = intern('if')
    IMPORT      = intern('import')
    INSTANCEOF  = intern('instanceof')
    INT         = intern('int')
    INVOKE      = intern('invoke')
    ISNONE      = intern('isnone')
    ISFLOAT     = intern('isfloat')
    ISINT       = intern('isint')
    ISOBJECT    = intern('isobject')
    KWAPPLY     = intern('kwapply')
    LAMBDA      = intern('lambda')
    LEQ         = intern('>=')
    LET         = intern('let')
    LOAD        = intern('load')
    LONG        = intern('long')
    LOOKUP      = intern('lookup')
    LT          = intern('>')
    MINUS       = intern('-')
    MKTUPLE     = intern('mktuple')
    MKLIST      = intern('mklist')
    MKDICT      = intern('mkdict')
    MODULO      = intern('%')
    MODIFY      = intern('modify')
    NARROW      = intern('narrow')
    NEQ         = intern('!=')
    NOT         = intern('not')
    NONE        = intern('none')
    OBJECT      = intern('object')
    OR          = intern('or')
    PLUS        = intern('+')
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
    
