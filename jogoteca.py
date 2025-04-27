# Importa as classes Flask e render_template do módulo flask.
# Flask é a classe principal para criar a aplicação web.
# render_template é uma função para renderizar arquivos HTML.
from flask import Flask, render_template

# Cria uma instância da classe Flask.
# __name__ é uma variável especial do Python que representa o nome do módulo atual.
# Isso é importante para o Flask encontrar arquivos estáticos e templates na pasta correta.
app = Flask(__name__)

# @app.route('/inicio') é um decorador do Flask.
# Ele associa a URL '/inicio' à função Python 'ola()'.
# Quando um usuário acessar 'http://seu_dominio/inicio' no navegador, a função 'ola()' será executada.
@app.route('/inicio')
def ola():
    # Esta função 'ola()' é chamada quando a rota '/inicio' é acessada.
    # 'render_template('lista.html')' usa a função render_template para procurar
    # um arquivo chamado 'lista.html' na pasta 'templates' (por padrão) e renderizá-lo.
    # O conteúdo desse arquivo HTML será retornado como a resposta para o navegador do usuário.
    return render_template('lista.html')

# app.run(debug=True) inicia o servidor de desenvolvimento do Flask.
# 'debug=True' habilita o modo de depuração. Isso significa que:
# 1. O servidor será reiniciado automaticamente sempre que você fizer alterações no código.
# 2. Informações de depuração detalhadas serão exibidas no navegador em caso de erros.
# É importante desativar o modo de depuração ('debug=False') em aplicações de produção.
app.run(debug=True)
