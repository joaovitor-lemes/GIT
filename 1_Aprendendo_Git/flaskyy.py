from flask import Flask

# Cria a aplicação Flask
app = Flask(__name__)

# Rota principal
@app.route('/')
def home():
    return 'Olá, mundo! Bem-vindo ao Flask, testando tudo'

# Roda a aplicação
if __name__ == '__main__':
    app.run(debug=True)

