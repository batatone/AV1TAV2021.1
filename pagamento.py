from pedido import Pedido

class Pagamento:
    def __init__(self, id, idpedido, vp, frete):
        self.id = int(id)
        self.idpedido = int(idpedido)
        self.vp = float(vp)
        self.frete = float(frete)

    def fazer(self, pedido):
        if type((pedido) == Pedido):
            vp = pedido.vt + pedido.frete
            frete = pedido.frete
            idp = pedido.id * 10 + 1
            idpedido = pedido.id
            pag = Pagamento(idp, idpedido, vp, frete)
            return pag
        else:
            return "Verifique o pedido inserido e tente novamente"