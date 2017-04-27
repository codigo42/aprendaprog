from time import strftime

from bottle import route, run

@route('/')
def hora():
    return strftime('%H:%M:%S')

run(host='localhost', port=8080, debug=True)
