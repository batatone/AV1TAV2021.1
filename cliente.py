from geopy.geocoders import Nominatim

class Cliente:
    def __init__(self, id, nome, endereco, lat, lon, idade, cpf):
        self.id = int(id)
        self.nome = str(nome)
        self.endereco = str(endereco)
        self.lat = float (lat)
        self.lon = float (lon)
        self.idade = int(idade)
        self.cpf = str(cpf)

    def cadastrar(id, nome, endereco, idade, cpf:int):
        nome=str(nome)
        nome = nome.capitalize()
        endereco = str(endereco)
        endereco = endereco.capitalize()
        if (id < 0):
            id = -259
            nome = "Erro de ID"
            endereco = "Erro de ID"
        if (idade > 150 or idade < 0):
            id = -260
            nome = "Erro de Idade"
            endereco = "Erro de Idade"
        scpf = str(cpf)
        lcpf = list(scpf)
        if (len(lcpf)!=11):
            return "Digite o CPF corretamente"
        else:
            lcpf.insert(3, ".")
            lcpf.insert(7, ".")
            lcpf.insert(11, "-")
            mcpf = ''.join(map(str, lcpf))

        geolocator = Nominatim(user_agent="test")
        location = geolocator.geocode(endereco)
        lat = location.latitude
        lon = location.longitude
        cli = Cliente(id, nome, endereco, lat, lon, idade, mcpf)
        return cli

