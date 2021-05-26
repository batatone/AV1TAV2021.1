from itenspedido import ItemPedido
from cliente import Cliente
from entrega import Entrega
import geopy
from geopy import distance

class Pedido:
    def __init__(self, id, idcliente, vt, identrega, frete):
        self.id = int(id)
        self.idcliente = int(idcliente)
        self.vt = float(vt)
        self.identrega = int(identrega)
        self.frete = float(frete)

    def calculafrete(lista, entrega):
        if (type(lista) == list):
            if (type(entrega) == Entrega):
                qtd = 0
                envio = (entrega.elat, entrega.elon)
                destino = (entrega.dlat, entrega.dlon)
                dist = geopy.distance.distance(envio, destino).km
                for x in lista:
                    if (type(x) != ItemPedido):
                        continue
                    else:
                        qtd = qtd + x.quantidade
                qtd = qtd * 5
                if (qtd > 50):
                    qtd = 50
                dist = dist / 100
                if (dist < 1):
                    dist = 1
                frete = dist * qtd
            else:
                return 0
        else:
            return 0
        return frete

    def fechar(lista, cliente, entrega):
        vtp = 0
        if (type(lista) == list):
            for x in lista:
                if (type(x) != ItemPedido):
                    continue
                else:
                    vtp = vtp + x.preco
            if (type(cliente) == Cliente and type(entrega) == Entrega):
                cli = cliente.id
                idp = (cliente.id * 1000000) + entrega.id
                ent = entrega.id
            else:
                return "Verifique os campos inseridos e tente novamente"

            ped = Pedido(idp, cli, vtp, ent, Pedido.calculafrete(lista, entrega))
        else:
            return "Verifique os itens do pedido e tente novamente"
        return ped