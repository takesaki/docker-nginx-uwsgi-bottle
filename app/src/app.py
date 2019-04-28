import bottle, jinja2
from bottle import route, run, default_app, jinja2_template as template 

bottle.TEMPLATE_PATH.append("./templates")
bottle.debug(True)

@route('<path:path>')
def index(path):
    return template('index.jt', uri=path)

if __name__ == '__main__':
    run(host='0.0.0.0', port=3031, debug=True, reloader=True)
else:
    application = default_app()
