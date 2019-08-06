from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hello, World!'

@app.route('/deneme')
def denemeMetodu():
	return 'DENEME!'

@app.route('/haber-<int:haberid>')
def haber_goster(haberid):
	return "Haber Detay" + str(haberid)
