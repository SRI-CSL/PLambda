import sys

class SymbolTable:

    _symbol_table = {
        sys.intern('and'):           sys.intern('and'),
        sys.intern('apply'):         sys.intern('apply'),
        sys.intern('array'):         sys.intern('array'),
        sys.intern('aset'):          sys.intern('aset'),
        sys.intern('boolean'):       sys.intern('boolean'),
        sys.intern('byte'):          sys.intern('byte'),
        sys.intern('catch'):         sys.intern('catch'),
        sys.intern('char'):          sys.intern('char'),
        sys.intern('concat'):        sys.intern('concat'),
        sys.intern('define'):        sys.intern('define'),
        sys.intern('/'):             sys.intern('/'),
        sys.intern('do'):            sys.intern('do'),
        sys.intern('double'):        sys.intern('double'),
        sys.intern('='):             sys.intern('='),
        sys.intern('=='):            sys.intern('=='),
        sys.intern('is'):            sys.intern('is'),
        sys.intern('fetch'):         sys.intern('fetch'),
        sys.intern('float'):         sys.intern('float'),
        sys.intern('for'):           sys.intern('for'),
        sys.intern('<='):            sys.intern('<='),
        sys.intern('get'):           sys.intern('get'),
        sys.intern('getattr'):       sys.intern('getattr'),
        sys.intern('getuid'):        sys.intern('getuid'),
        sys.intern('global'):        sys.intern('global'),
        sys.intern('<'):             sys.intern('<'),
        sys.intern('if'):            sys.intern('if'),
        sys.intern('import'):        sys.intern('import'),
        sys.intern('instanceof'):    sys.intern('instanceof'),
        sys.intern('int'):           sys.intern('int'),
        sys.intern('invoke'):        sys.intern('invoke'),
        sys.intern('isnone'):        sys.intern('isnone'),
        sys.intern('isfloat'):       sys.intern('isfloat'),
        sys.intern('isint'):         sys.intern('isint'),
        sys.intern('isobject'):      sys.intern('isobject'),
        sys.intern('kwapply'):       sys.intern('kwapply'),
        sys.intern('lambda'):        sys.intern('lambda'),
        sys.intern('>='):            sys.intern('>='),
        sys.intern('let'):           sys.intern('let'),
        sys.intern('load'):          sys.intern('load'),
        sys.intern('long'):          sys.intern('long'),
        sys.intern('lookup'):        sys.intern('lookup'),
        sys.intern('>'):             sys.intern('>'),
        sys.intern('-'):             sys.intern('-'),
        sys.intern('mktuple'):       sys.intern('mktuple'),
        sys.intern('mklist'):        sys.intern('mklist'),
        sys.intern('mkdict'):        sys.intern('mkdict'),
        sys.intern('modify'):        sys.intern('modify'),
        sys.intern('%'):             sys.intern('%'),
        sys.intern('narrow'):        sys.intern('narrow'),
        sys.intern('!='):            sys.intern('!='),
        sys.intern('not'):           sys.intern('not'),
        sys.intern('none'):          sys.intern('none'),
        sys.intern('object'):        sys.intern('object'),
        sys.intern('or'):            sys.intern('or'),
        sys.intern('+'):             sys.intern('+'),
        sys.intern('seq'):           sys.intern('seq'),
        sys.intern('setattr'):       sys.intern('setattr'),
        sys.intern('setuid'):        sys.intern('setuid'),
        sys.intern('short'):         sys.intern('short'),
        sys.intern('sinvoke'):       sys.intern('sinvoke'),
        sys.intern('supdate'):       sys.intern('supdate'),
        sys.intern('throw'):         sys.intern('throw'),
        sys.intern('*'):             sys.intern('*'),
        sys.intern('try'):           sys.intern('try'),
        sys.intern('update'):        sys.intern('update'),
        }


    AND         = sys.intern('and')
    APPLY       = sys.intern('apply')
    ARRAY       = sys.intern('array')
    ASET        = sys.intern('aset')
    BOOLEAN     = sys.intern('boolean')
    BYTE        = sys.intern('byte')
    CATCH       = sys.intern('catch')
    CHAR        = sys.intern('char')
    CONCAT      = sys.intern('concat')
    DEFINE      = sys.intern('define')
    DIVIDE      = sys.intern('/')
    DO          = sys.intern('do')
    DOUBLE      = sys.intern('double')
    IS          = sys.intern('is')
    EQUALS      = sys.intern('=')
    EQ          = sys.intern('==')
    FETCH       = sys.intern('fetch')
    FLOAT       = sys.intern('float')
    FOR         = sys.intern('for')
    GEQ         = sys.intern('>=')
    GET         = sys.intern('get')
    GETATTR     = sys.intern('getattr')
    GETUID      = sys.intern('getuid')
    GLOBAL      = sys.intern('global')
    GT          = sys.intern('<')
    IF          = sys.intern('if')
    IMPORT      = sys.intern('import')
    INSTANCEOF  = sys.intern('instanceof')
    INT         = sys.intern('int')
    INVOKE      = sys.intern('invoke')
    ISNONE      = sys.intern('isnone')
    ISFLOAT     = sys.intern('isfloat')
    ISINT       = sys.intern('isint')
    ISOBJECT    = sys.intern('isobject')
    KWAPPLY     = sys.intern('kwapply')
    LAMBDA      = sys.intern('lambda')
    LEQ         = sys.intern('<=')
    LET         = sys.intern('let')
    LOAD        = sys.intern('load')
    LONG        = sys.intern('long')
    LOOKUP      = sys.intern('lookup')
    LT          = sys.intern('>')
    MINUS       = sys.intern('-')
    MKTUPLE     = sys.intern('mktuple')
    MKLIST      = sys.intern('mklist')
    MKDICT      = sys.intern('mkdict')
    MODULO      = sys.intern('%')
    MODIFY      = sys.intern('modify')
    NARROW      = sys.intern('narrow')
    NEQ         = sys.intern('!=')
    NOT         = sys.intern('not')
    NONE        = sys.intern('none')
    OBJECT      = sys.intern('object')
    OR          = sys.intern('or')
    PLUS        = sys.intern('+')
    SEQ         = sys.intern('seq')
    SETATTR     = sys.intern('setattr')
    SETUID      = sys.intern('setuid')
    SHORT       = sys.intern('short')
    SINVOKE     = sys.intern('sinvoke')
    SUPDATE     = sys.intern('supdate')
    THROW       = sys.intern('throw')
    TIMES       = sys.intern('*')
    TRY         = sys.intern('try')
    UPDATE      = sys.intern('update')

    @staticmethod
    def canonicalize(name):
        return SymbolTable._symbol_table.get(name.lower())
