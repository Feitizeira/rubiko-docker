from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/', methods=['GET'])
def landing_page():
    greeting = os.environ.get('GREETINGS', 'Servidor en funcionamiento')
    return render_template('template/landing_page.html', greeting=greeting)

@app.route('/health', methods=['GET'])
def health_check():
    greeting = os.environ.get('GREETINGS', 'Servidor en funcionamiento')
    return greeting, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

