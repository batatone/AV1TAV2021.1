class Entrega:
    def __init__(self, id, idpedido, idcliente, elat, elon, dlat, dlon):
        self.id = int(id)
        self.idpedido = int(idpedido)
        self.idpedido = int(idcliente)
        self.elat = float (elat)
        self.elon = float (elon)
        self.dlat = float (dlat)
        self.dlon = float (dlon)
