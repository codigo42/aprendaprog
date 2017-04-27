from time import strftime

from bottle import route, run, response

@route('/')
def hora():
    response.set_header('Refresh', '1')
    return strftime('%H:%M:%S')

run(host='localhost', port=8080, debug=True)
