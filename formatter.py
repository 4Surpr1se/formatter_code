from pygments import highlight
from pygments import lexers
from pygments.formatters.img import ImageFormatter
from pygments.styles import get_style_by_name, STYLE_MAP

print(STYLE_MAP)  # styles - https://pygments.org/styles/

lexer = lexers.get_lexer_by_name('python')
with open('init.py', 'r') as f:
    init = f.read().ljust(80, ' ')
formatter = ImageFormatter(image_format='jpeg', full=True, style=get_style_by_name('lightbulb'))
highlight(init, lexer, formatter, 'init.jpeg')
