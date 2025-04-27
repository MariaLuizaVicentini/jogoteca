# importar a classe Flask da framework flask
from flask import Flask

# Criando um objeto da classe Flask.
# __name__ é uma variável especial do Python que representa o nome do módulo atual.
# Ao passar __name__, o Flask sabe onde procurar por arquivos estáticos e templates.
app = Flask(__name__)

# @app.route('/inicio') é um decorador do Flask.
# Ele associa a URL '/inicio' à função Python 'ola()'.
# Quando um usuário acessar 'http://seu_dominio/inicio' no navegador, a função 'ola()' será executada.
@app.route('/inicio')
def ola():
    # Esta função 'ola()' é chamada quando a rota '/inicio' é acessada.
    # 'return '<h1>Olá Flask!</h1>'' faz com que o servidor Flask envie uma resposta HTTP
    # com o conteúdo '<h1>Olá Flask!</h1>' para o navegador do usuário.
    # A tag '<h1>' indica um cabeçalho de nível 1 em HTML.
    return '<h1>Olá Flask!</h1>'

# app.run(debug=True) inicia o servidor de desenvolvimento do Flask.
# 'debug=True' habilita o modo de depuração. Isso significa que:
# 1. O servidor será reiniciado automaticamente sempre que você fizer alterações no código.
# 2. Informações de depuração detalhadas serão exibidas no navegador em caso de erros.
# É importante desativar o modo de depuração ('debug=False') em aplicações de produção.
app.run(debug=True)
