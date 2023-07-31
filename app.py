from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        'id': 1,
        'title': 'A Volta dos que Não Foram - O Retorno',
        'autor': 'Desconhecido'
    },
    {
        'id': 2,
        'title': 'A Loucura das Segundas-Feiras: Sobrevivendo ao Começo da Semana',
        'autor': 'Mário Maluco'
    },
    {
        'id': 3,
        'title': 'Pegando Chuva com Estilo: A Arte da Dança dos Guarda-Chuvas',
        'autor': 'Sofia Ensopadinha'
    }
]


@app.route('/livros', methods=['GET'])
def obter_livros():
    return jsonify(livros)


# consultar id

@app.route('/livros/<int:id>', methods=['GET'])
def obter_livro_por_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)


# editar livro por id

@app.route('/livros/<int:id>', methods=['PUT'])
def editar_livro_por_id(id):
    livro_alterado = request.get_json()
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])

# criar livro


@app.route('/livros', methods=['POST'])
def criar_novo_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)

    return jsonify(livros)


@app.route('/livros/<int:id>', methods=['DELETE'])
def excluir_livro(id):
   for indice, livro in enumerate(livros):
    if livro.get('id') == id:
        del livros[indice]

        return jsonify(livros)

if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=True)
