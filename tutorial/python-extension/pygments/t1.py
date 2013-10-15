from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.lexers import get_lexer_by_name,get_lexer_for_filename,get_lexer_for_mimetype
from pygments.formatters import HtmlFormatter

code = 'print "hello world"'
result = highlight(code,PythonLexer(),HtmlFormatter())
print(result)
#print(HtmlFormatter().get_style_defs('.highlight'))

lexer = get_lexer_by_name('python',stripall=True)
formatter = HtmlFormatter(linenos=True,cssclass='source')
result = highlight(code,lexer,formatter)
print(result)

lexer = get_lexer_by_name('python')
print(lexer)
lexer = get_lexer_for_filename('test.py')
print(lexer)
lexer = get_lexer_for_mimetype('text/x-perl')
print(lexer)


