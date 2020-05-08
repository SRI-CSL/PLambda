from ..crap.py import plambda_intern

class SymbolTable:

    _symbol_table = {
        plambda_intern('and'):           plambda_intern('and'),
        plambda_intern('apply'):         plambda_intern('apply'),
        plambda_intern('array'):         plambda_intern('array'),
        plambda_intern('aset'):          plambda_intern('aset'),
        plambda_intern('boolean'):       plambda_intern('boolean'),
        plambda_intern('byte'):          plambda_intern('byte'),
        plambda_intern('catch'):         plambda_intern('catch'),
        plambda_intern('char'):          plambda_intern('char'),
        plambda_intern('concat'):        plambda_intern('concat'),
        plambda_intern('define'):        plambda_intern('define'),
        plambda_intern('/'):             plambda_intern('/'),
        plambda_intern('do'):            plambda_intern('do'),
        plambda_intern('double'):        plambda_intern('double'),
        plambda_intern('='):             plambda_intern('='),
        plambda_intern('=='):            plambda_intern('=='),
        plambda_intern('is'):            plambda_intern('is'),
        plambda_intern('fetch'):         plambda_intern('fetch'),
        plambda_intern('float'):         plambda_intern('float'),
        plambda_intern('for'):           plambda_intern('for'),
        plambda_intern('<='):            plambda_intern('<='),
        plambda_intern('get'):           plambda_intern('get'),
        plambda_intern('getattr'):       plambda_intern('getattr'),
        plambda_intern('getuid'):        plambda_intern('getuid'),
        plambda_intern('global'):        plambda_intern('global'),
        plambda_intern('<'):             plambda_intern('<'),
        plambda_intern('if'):            plambda_intern('if'),
        plambda_intern('import'):        plambda_intern('import'),
        plambda_intern('instanceof'):    plambda_intern('instanceof'),
        plambda_intern('int'):           plambda_intern('int'),
        plambda_intern('invoke'):        plambda_intern('invoke'),
        plambda_intern('isnone'):        plambda_intern('isnone'),
        plambda_intern('isfloat'):       plambda_intern('isfloat'),
        plambda_intern('isint'):         plambda_intern('isint'),
        plambda_intern('isobject'):      plambda_intern('isobject'),
        plambda_intern('kwapply'):       plambda_intern('kwapply'),
        plambda_intern('lambda'):        plambda_intern('lambda'),
        plambda_intern('>='):            plambda_intern('>='),
        plambda_intern('let'):           plambda_intern('let'),
        plambda_intern('load'):          plambda_intern('load'),
        plambda_intern('long'):          plambda_intern('long'),
        plambda_intern('lookup'):        plambda_intern('lookup'),
        plambda_intern('>'):             plambda_intern('>'),
        plambda_intern('-'):             plambda_intern('-'),
        plambda_intern('mktuple'):       plambda_intern('mktuple'),
        plambda_intern('mklist'):        plambda_intern('mklist'),
        plambda_intern('mkdict'):        plambda_intern('mkdict'),
        plambda_intern('modify'):        plambda_intern('modify'),
        plambda_intern('%'):             plambda_intern('%'),
        plambda_intern('narrow'):        plambda_intern('narrow'),
        plambda_intern('!='):            plambda_intern('!='),
        plambda_intern('not'):           plambda_intern('not'),
        plambda_intern('none'):          plambda_intern('none'),
        plambda_intern('object'):        plambda_intern('object'),
        plambda_intern('or'):            plambda_intern('or'),
        plambda_intern('+'):             plambda_intern('+'),
        plambda_intern('seq'):           plambda_intern('seq'),
        plambda_intern('setattr'):       plambda_intern('setattr'),
        plambda_intern('setuid'):        plambda_intern('setuid'),
        plambda_intern('short'):         plambda_intern('short'),
        plambda_intern('sinvoke'):       plambda_intern('sinvoke'),
        plambda_intern('supdate'):       plambda_intern('supdate'),
        plambda_intern('throw'):         plambda_intern('throw'),
        plambda_intern('*'):             plambda_intern('*'),
        plambda_intern('try'):           plambda_intern('try'),
        plambda_intern('update'):        plambda_intern('update'),
        }


    AND         = plambda_intern('and')
    APPLY       = plambda_intern('apply')
    ARRAY       = plambda_intern('array')
    ASET        = plambda_intern('aset')
    BOOLEAN     = plambda_intern('boolean')
    BYTE        = plambda_intern('byte')
    CATCH       = plambda_intern('catch')
    CHAR        = plambda_intern('char')
    CONCAT      = plambda_intern('concat')
    DEFINE      = plambda_intern('define')
    DIVIDE      = plambda_intern('/')
    DO          = plambda_intern('do')
    DOUBLE      = plambda_intern('double')
    IS          = plambda_intern('is')
    EQUALS      = plambda_intern('=')
    EQ          = plambda_intern('==')
    FETCH       = plambda_intern('fetch')
    FLOAT       = plambda_intern('float')
    FOR         = plambda_intern('for')
    GEQ         = plambda_intern('<=')
    GET         = plambda_intern('get')
    GETATTR     = plambda_intern('getattr')
    GETUID      = plambda_intern('getuid')
    GLOBAL      = plambda_intern('global')
    GT          = plambda_intern('<')
    IF          = plambda_intern('if')
    IMPORT      = plambda_intern('import')
    INSTANCEOF  = plambda_intern('instanceof')
    INT         = plambda_intern('int')
    INVOKE      = plambda_intern('invoke')
    ISNONE      = plambda_intern('isnone')
    ISFLOAT     = plambda_intern('isfloat')
    ISINT       = plambda_intern('isint')
    ISOBJECT    = plambda_intern('isobject')
    KWAPPLY     = plambda_intern('kwapply')
    LAMBDA      = plambda_intern('lambda')
    LEQ         = plambda_intern('>=')
    LET         = plambda_intern('let')
    LOAD        = plambda_intern('load')
    LONG        = plambda_intern('long')
    LOOKUP      = plambda_intern('lookup')
    LT          = plambda_intern('>')
    MINUS       = plambda_intern('-')
    MKTUPLE     = plambda_intern('mktuple')
    MKLIST      = plambda_intern('mklist')
    MKDICT      = plambda_intern('mkdict')
    MODULO      = plambda_intern('%')
    MODIFY      = plambda_intern('modify')
    NARROW      = plambda_intern('narrow')
    NEQ         = plambda_intern('!=')
    NOT         = plambda_intern('not')
    NONE        = plambda_intern('none')
    OBJECT      = plambda_intern('object')
    OR          = plambda_intern('or')
    PLUS        = plambda_intern('+')
    SEQ         = plambda_intern('seq')
    SETATTR     = plambda_intern('setattr')
    SETUID      = plambda_intern('setuid')
    SHORT       = plambda_intern('short')
    SINVOKE     = plambda_intern('sinvoke')
    SUPDATE     = plambda_intern('supdate')
    THROW       = plambda_intern('throw')
    TIMES       = plambda_intern('*')
    TRY         = plambda_intern('try')
    UPDATE      = plambda_intern('update')

    @staticmethod
    def canonicalize(name):
        return SymbolTable._symbol_table.get(name.lower())
