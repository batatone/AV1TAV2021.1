class Produto:
    def __init__(self, id, nome, quantidade, preco, fornecedor):
        self.id = int(id)
        self.nome = str(nome)
        self.quantidade = int(quantidade)
        self.preco = float(preco)
        self.fornecedor = str(fornecedor)

    def create(id, nome, quantidade, preco, fornecedor):
        nome = nome.capitalize()

        fornecedor = fornecedor.capitalize()

        if (preco<=0):
            preco = -800
            nome = "Erro de Preço"
            fornecedor = "Erro"

        if (id%10==0 or id<0):
            id = -255
            nome = "Erro de ID"
            fornecedor = "Erro"

        if (id==-255 and preco==-800):
            id = -999
            nome = "Erro Múltiplo"
            fornecedor = "Erro"

        if (quantidade<0):
            quantidade = 0

        produto = Produto(id,nome,quantidade,preco,fornecedor)

        return produto