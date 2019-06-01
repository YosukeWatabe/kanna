from bottle import route, run, template, request,static_file
from chat import chat


@route('/hello')
def hello():
    return template('chatbot.html', input_text='', output_text='')

@route('/hello', method='POST')
def do_hello():
    input_text = request.forms.input_text
    output_text = chat(input_text)
    return template('chatbot.html', input_text=input_text, output_text=output_text)

run(host='localhost', port=8080, reloader=True, debug=True)