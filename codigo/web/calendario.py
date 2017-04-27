from time import localtime
from calendar import HTMLCalendar

from bottle import route, run, response, template

HTML = '''
<html>
  <head>
    <meta charset="utf-8">
    <title>Calendário</title>
  </head>
  <body>
    <h1>Calendário do mês {{mes}}/{{ano}}</h1>
    {{!calendario}}
  </body>
</html>
'''

@route('/')
def mes():
    calendario = HTMLCalendar()
    ano, mes = localtime()[:2]
    html_mes = calendario.formatmonth(ano, mes)
    return template(HTML, ano=ano, mes=mes, calendario=html_mes)

run(host='localhost', port=8080, debug=True)
