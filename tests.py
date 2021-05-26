import unittest

import geopy
from geopy import Nominatim
from unittest.mock import patch
from carrinho import Carrinho
from cliente import Cliente
from itenspedido import ItemPedido
from itenscarrinho import ItemCarrinho
from pedido import Pedido
from entrega import Entrega
from pagamento import Pagamento

class teste(unittest.TestCase):
    def test_adicionaitem(self):
        item = ItemCarrinho(1,1,1,1,1,1)
        car = Carrinho(1,0,0,0,0,0)
        car = Carrinho.additem(item,car)

        self.assertEqual(car.freteq, 1)

        item2 = ItemCarrinho(1,1,1,2,1,1)
        car = Carrinho.additem(item2,car)

        self.assertEqual(car.freteq, 3)

        item3 = ItemCarrinho(1,0,1,1,1,1)
        car = Carrinho.additem(item3,car)

        self.assertEqual(car.freteq, 3)

        item4="Esse falha"
        car = Carrinho.additem(item4,car)

        self.assertEqual(car.freteq, 3)

        car2="Esse falha grave"
        car = Carrinho.additem(item3,car2)

        self.assertEqual(car, "Esse falha grave")

    def test_simulafrete(self):
        car = Carrinho(1,0,0,1,1,1)
        car = Carrinho.simulafrete(car)

        self.assertEqual(car.fretes, 5)

        car = Carrinho(1,0,0,1,40,1)
        car = Carrinho.simulafrete(car)

        self.assertEqual(car.fretes, 50)

        car = Carrinho(1,0,0,1,90,1)
        car = Carrinho.simulafrete(car)

        self.assertEqual(car.fretes, 50)

        car2 = "Falha"
        car2 = Carrinho.simulafrete(car2)

        self.assertEqual(car2, "Falha")


    def test_calculafrete(self):
        lista=[]
        lista.append(ItemPedido(1,1,1,1,1))
        lista.append(ItemPedido(1,1,1,1,1))
        lista.append(ItemPedido(1,1,1,1,1))
        lista.append(ItemPedido(1,1,1,1,1))
        lista.append(ItemPedido(1,1,1,1,1))
        entrega = Entrega(1,1,1,10,10,20,20)
        frete = Pedido.calculafrete(lista,entrega)

        self.assertEqual(frete, 385.4641084875731)

        entrega2 = Entrega(1,1,1,10,10,10,10)
        frete = Pedido.calculafrete(lista,entrega2)

        self.assertEqual(frete, 25)

        entrega3 = "falha"
        frete = Pedido.calculafrete(lista,entrega3)

        self.assertEqual(frete, 0)

        lista2 = "falha"
        frete = Pedido.calculafrete(lista2,entrega2)

        self.assertEqual(frete, 0)

    @patch.object(Pedido, 'calculafrete')
    def test_fecharpedido(self, mock_calculafrete):
        mock_calculafrete.return_value=100
        lista=[]
        lista.append(ItemPedido(1,1,1,1,1))
        lista.append(ItemPedido(1,1,1,1,1))
        lista.append(ItemPedido(1,1,1,1,1))
        lista.append(ItemPedido(1,1,1,1,1))
        lista.append(ItemPedido(1,1,1,1,1))
        entrega = Entrega(1,1,1,10,10,20,20)
        cliente = Cliente(1,1,1,10,10,1,1)
        pedido = Pedido.fechar(lista,cliente,entrega)

        self.assertEqual(type(pedido), Pedido)
        self.assertEqual(pedido.frete, 100)
        self.assertEqual(pedido.vt, 5)

        entrega2 = "falha"
        pedido = Pedido.fechar(lista, cliente, entrega2)

        self.assertEqual(type(pedido), str)


        cliente2 = "falha"
        pedido = Pedido.fechar(lista, cliente2, entrega)

        self.assertEqual(type(pedido), str)

        lista2 = "falha"
        pedido = Pedido.fechar(lista2, cliente, entrega)

        self.assertEqual(type(pedido), str)

    def test_fazerpagamento(self):
        pedido = Pedido(1,1,1,1,1)
        pag = Pagamento.fazer(pedido)

        self.assertEqual(type(pag), Pagamento)
        self.assertEqual(pag.vp, 2)

        pedido = "falha"
        pag = Pagamento.fazer(pedido)

        self.assertEqual(type(pag), str)

    @patch.object(Nominatim, 'geocode')
    def test_cadastracliente(self, mock_geocode):
        mock_geocode.return_value = geopy.location.Location("Rua Domingos Freire, Todos os Santos, \
        Zona Norte do Rio de Janeiro, Rio de Janeiro, Região Geográfica Imediata do Rio de Janeiro, \
        Região Metropolitana do Rio de Janeiro, Região Geográfica Intermediária do Rio de Janeiro, \
        Rio de Janeiro, Região Sudeste, 20735080, Brasil","22 53m 57.0473s S, 43 17m 3.7302s W", "{'place_id': \
        147571997, 'licence': 'Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright', \
        'osm_type': 'way', 'osm_id': 233207603, 'boundingbox': ['-22.8991798', '-22.898734', '-43.2852869', \
        '-43.2843695'], 'lat': '-22.8991798', 'lon': '-43.2843695', 'display_name': 'Rua Domingos Freire, \
        Todos os Santos, Zona Norte do Rio de Janeiro, Rio de Janeiro, Região Geográfica Imediata do Rio de Janeiro, \
        Região Metropolitana do Rio de Janeiro, Região Geográfica Intermediária do Rio de Janeiro, Rio de Janeiro, \
        Região Sudeste, 20735080, Brasil', 'class': 'highway', 'type': 'residential', 'importance': 0.4}")
        cliente = Cliente.cadastrar(1,1,1,1,12345678901)

        self.assertEqual(type(cliente), Cliente)
        self.assertEqual(cliente.cpf, "123.456.789-01")

        cliente2 = Cliente.cadastrar(1, 1, 1, 1, 123456789)

        self.assertEqual(type(cliente2), str)

        cliente3 = Cliente.cadastrar(-1, 1, 1, 1, 12345678901)

        self.assertEqual(cliente3.id, -259)
        self.assertEqual(cliente3.nome, "Erro de ID")

        cliente4 = Cliente.cadastrar(1, 1, 1, -1, 12345678901)

        self.assertEqual(cliente4.id, -260)
        self.assertEqual(cliente4.nome, "Erro de Idade")

        cliente5 = Cliente.cadastrar(1, 1, 1, 999, 12345678901)

        self.assertEqual(cliente5.id, -260)
        self.assertEqual(cliente5.nome, "Erro de Idade")
