class ItemPedido:
    def __init__(self, id, idpedido, idcarrinho, quantidade, preco):
        self.id = int(id)
        self.idpedido = int(idpedido)
        self.idproduto = int(idcarrinho)
        self.quantidade = int(quantidade)
        self.preco = float(preco)

    def create (id, idpedido, idproduto, quantidade, preco):
        if (id<0):
            id = -253

        if (id or idproduto<0):
            item = "Erro"
        else:
            item = ItemPedido(id, idpedido, idproduto, quantidade, preco)

        return item