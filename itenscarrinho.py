class ItemCarrinho:
    def __init__(self, id, idcarrinho, idproduto, quantidade, preco, nome):
        self.id = int(id)
        self.idcarrinho = int(idcarrinho)
        self.idproduto = int(idproduto)
        self.quantidade = int(quantidade)
        self.preco = float(preco)
        self.nome = str(nome)

    def create (id, idcarrinho, idproduto, quantidade, preco, nome):
        if (id<0):
            id = -254

        if (id or idproduto<0):
            item = "Erro"
        else:
            item = ItemCarrinho(id, idcarrinho, idproduto, quantidade, preco, nome)

        return item