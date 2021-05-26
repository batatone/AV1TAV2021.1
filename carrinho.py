#cep destino cep origem peso

from itenscarrinho import ItemCarrinho
import datetime

class Carrinho:
    def __init__(self, id, datac, vt, frete, freteq, fretes):
        self.id = int(id)
        self.datac = datac
        self.vt = float(vt)
        self.frete = float(frete)
        self.freteq = int(freteq)
        self.fretes = float(fretes)

    def create(lista):
        if (type(lista) == list):
            lista.append(Carrinho(len(lista), datetime.datetime.now(), 0, 0, 0, 0))
        else:
            lista = [Carrinho(len(lista), datetime.datetime.now(), 0, 0, 0, 0)]
        return lista

    def additem(item,carrinho):
        if (type(item) == ItemCarrinho and type(carrinho) == Carrinho):
            if (item.idcarrinho == carrinho.id):
                car = Carrinho(carrinho.id, carrinho.datac, carrinho.vt, carrinho.frete, carrinho.freteq, carrinho.fretes)
                car.vt = carrinho.vt + item.preco
                car.freteq = carrinho.freteq + item.quantidade
            else:
                car = Carrinho(carrinho.id, carrinho.datac, carrinho.vt, carrinho.frete, carrinho.freteq, carrinho.fretes)
            return car
        else:
            return "Verifique os itens inseridos e tente novamente"

    def simulafrete(carrinho):
        if (type(carrinho) == Carrinho):
            carrinho.fretes = carrinho.freteq * 5
            if (carrinho.fretes > 50):
                carrinho.fretes = 50
            car = Carrinho(carrinho.id, carrinho.datac, carrinho.vt, carrinho.frete, carrinho.freteq, carrinho.fretes)
            return car
        else:
            return carrinho