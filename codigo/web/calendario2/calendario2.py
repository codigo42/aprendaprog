from time import localtime
from calendar import LocaleHTMLCalendar

from bottle import route, run, response, template, static_file

HTML = '''
<html>
  <head>
    <meta charset="utf-8">
    <title>Calendário</title>
    <link rel="stylesheet" href="static/estilo.css">
  </head>
  <body>
    <h1>Calendário do mês {{mes}} de {{ano}}</h1>
    {{!calendario}}
  </body>
</html>
'''

@route('/')
def mes():
    ano, mes = localtime()[:2]
    calendario = LocaleHTMLCalendar(locale='pt_BR.utf8')
    html_mes = calendario.formatmonth(ano, mes)
    return template(HTML, ano=ano, mes=mes, calendario=html_mes)

@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='static')

run(host='localhost', port=8080, debug=True)
