from django import template
import mistune
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter

register = template.Library()

class HighlightRenderer(mistune.Renderer):
    def block_code(self, code, lang):
#        if not lang:
        return '\n<pre class="brush: %s">%s</pre>\n' % \
                (lang, mistune.escape(code))
        #lexer = get_lexer_by_name(lang, stripall=True)
        #formatter = HtmlFormatter()
        #self.info = "code: %s | lexer: %s | formatter: %s" % (code, lexer, formatter)
#        return highlight(code, lexer, formatter)
renderer = HighlightRenderer()
markdown = mistune.Markdown(renderer=renderer)
print(markdown('```python\nassert 1 == 1\n```'))

@register.filter
def markdown(value):
    renderer = HighlightRenderer()
    markdown = mistune.Markdown(renderer=renderer)
    return markdown(value)
