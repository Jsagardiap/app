# Definicion inicial de aplicacion
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/test')
def test():
    return render_template('prueba.html')

@app.route('/autentica', methods = ['POST', 'GET'])
def autentica():
    if request.method == 'POST':
        rut_Rec = request.form['usuario']
        pas_Rec = request.form['clave']
        if (rut_Rec == '9913518-2' and pas_Rec == 'Ingreso'):
            return render_template('mensaje.html')
        else:
            return render_template('prueba.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
