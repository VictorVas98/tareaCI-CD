from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "<h1>Bienvenido a mi Despliegue Automático en Azure</h1><p>Versión 1.0</p>"

if __name__ == '__main__':
    app.run()