from itenspedido import ItemPedido
from cliente import Cliente
from entrega import Entrega
import geopy

class Pedido:
    def __init__(self, id, idcliente, vt, identrega, frete):
        self.id = int(id)
        self.idcliente = int(idcliente)
        self.vt = float(vt)
        self.identrega = int(identrega)
        self.frete = float(frete)

    def calculafrete(lista, entrega):
        if (type(lista) == list):
            if type((entrega) == Entrega):
                envio = (entrega.elat, entrega.elon)
                destino = (entrega.dlat, entrega.dlon)
                dist = geopy.distance.distance(envio, destino).km
                for x in lista:
                    if (type(x) != ItemPedido):
                        del lista[lista.index(x)]
                        continue
                    else:
                        qtd = qtd + x.quantidade
                qtd = qtd * 5
                if (qtd > 50):
                    qtd = 50
                dist = dist / 100
                if (dist < 1):
                    dist = 1
                frete = dist + qtd
            else:
                return "Verifique o campo entrega e tente novamente"
        else:
            return "Verifique se o objeto inserido é uma lista e tente novamente"
        return frete

    def fechar(lista, cliente, entrega):
        if (type(lista) == list):
            for x in lista:
                if (type(x) != ItemPedido):
                    del lista[lista.index(x)]
                    continue
                else:
                    vtp = vtp + x.preco
            idp = (cliente.id * 1000000) + entrega.id
            if (type(cliente) == Cliente):
                cli = cliente.id
            else:
                return "Verifique o campo cliente e tente novamente"
            if (type(entrega) == Entrega):
                ent = entrega.id
            else:
                return "Verifique o campo entrega e tente novamente"
            ped = Pedido(idp, cli, vtp, ent, Pedido.calculafrete(lista, entrega))
        return ped
    
