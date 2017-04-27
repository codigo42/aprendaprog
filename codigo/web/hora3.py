from time import strftime

from bottle import route, run, response, template

HTML = '''
<html>
  <head>
    <meta charset="utf-8">
    <title>Hora: {{hora}}</title>
  </head>
  <body>
    <h1>{{hora}}</h1>
  </body>
</html>
'''

@route('/')
def hora():
    response.set_header('Refresh', '1')
    hora = strftime('%H:%M:%S')
    return template(HTML, hora=hora)

run(host='localhost', port=8080, debug=True)
