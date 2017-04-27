from time import localtime
from calendar import LocaleHTMLCalendar

from bottle import route, run, response, template, static_file

HTML = '''
<html>
  <head>
    <meta charset="utf-8">
    <title>Calendário</title>
    <link rel="stylesheet" href="/static/estilo.css">
  </head>
  <body>
    <h1>Calendário do mês {{mes}} de {{ano}}</h1>
    {{!calendario}}
    <hr>
    <a href="/{{prox_mes}}">{{prox_mes}}</a>
  </body>
</html>
'''

def prox_mes(ano, mes):
    if mes < 12:
        mes += 1
    else:
        ano += 1
        mes = 1
    return '%04d/%02d' % (ano, mes)

@route('/')
@route('/<ano:int>')
@route('/<ano:int>/<mes:int>')
def mes(ano=None, mes=None):
    if ano is None:
        ano, mes = localtime()[:2]
    elif mes is None:
        mes = localtime()[1]
    calendario = LocaleHTMLCalendar(locale='pt_BR.utf8')
    html_mes = calendario.formatmonth(ano, mes)
    return template(HTML, ano=ano, mes=mes,
                          calendario=html_mes, prox_mes=prox_mes(ano, mes))

@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='static')

run(host='localhost', port=8080, debug=True)
