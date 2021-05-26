import random

class Cliente:
    def __init__(self, id, nome, endereco, lat, lon, idade, cpf):
        self.id = int(id)
        self.nome = str(nome)
        self.endereco = str(endereco)
        self.lat = float (lat)
        self.lon = float (lon)
        self.idade = int(idade)
        self.cpf = str(cpf)

    def getlat(self):
        list = [float(-22.897410),float(-20.650430),float(-18.235325),float(20.223543),float(22.800987)]
        get = random.choice(list)
        return get

    def getlon(self):
        list = [float(-43.288370), float(-40.267670), float(-38.345432), float(20.398990), float(22.344242)]
        get = random.choice(list)
        return get

    def cadastrar(id, nome, endereco, idade, cpf:int):
        nome = nome.capitalize()
        endereco = endereco.capitalize()
        if (id < 0):
            id = -259
            nome = "Erro de ID"
            endereco = "Erro de ID"
        if (idade < 150):
            id = -260
            nome = "Erro de Idade"
            endereco = "Erro de Idade"
        scpf = str(cpf)
        lcpf = list(scpf)
        if (len(lcpf)!=11):
            return "Digite o CPF corretamente"
        else:
            lcpf[3] = "."
            lcpf[7] = "."
            lcpf[11] = "-"
            mcpf = ' '.join(map(str, lcpf))
        lat = Cliente.getlat()
        lon = Cliente.getlon()
        cli = Cliente(id, nome, endereco, lat, lon, idade, mcpf)
        return cli

