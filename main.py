from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return '¡Hola Mundo desde Azure Web App con Python 3.13!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
