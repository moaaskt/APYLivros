from flask import Flask, jsonify, request, make_response

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
    return jsonify(livros), 200

@app.route('/livros/<int:id>', methods=['GET'])
def obter_livro_por_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro), 200
    return jsonify({'mensagem': 'Livro não encontrado'}), 404

@app.route('/livros/<int:id>', methods=['PUT'])
def editar_livro_por_id(id):
    livro_alterado = request.get_json()
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice]), 200
    return jsonify({'mensagem': 'Livro não encontrado'}), 404

@app.route('/livros', methods=['POST'])
def criar_novo_livro():
    novo_livro = request.get_json()
    if 'title' not in novo_livro or 'autor' not in novo_livro:
        return jsonify({'mensagem': 'Campos title e autor são obrigatórios'}), 400

    novo_livro['id'] = len(livros) + 1
    livros.append(novo_livro)
    return jsonify({'mensagem': 'Livro Cadastrado com sucesso'}), 200
    return jsonify(novo_livro), 201 
    

@app.route('/livros/<int:id>', methods=['DELETE'])
def excluir_livro(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]
            return jsonify({'mensagem': 'Livro excluído com sucesso'}), 200
    return jsonify({'mensagem': 'Livro não encontrado'}), 404

if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=True)
