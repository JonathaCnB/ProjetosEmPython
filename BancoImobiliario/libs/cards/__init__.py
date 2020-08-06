class card_titulo_posse:

    def __init__(self, preco_card, aluguel_card, preco_uma_casa, preco_duas_casas, preco_tres_casas, preco_quatro_casas, preco_hotel, preco_construir, preco_hipoteca,
                 hipotecada, dono, regiao):
        self.preco_card = preco_card
        self.aluguel_card = aluguel_card
        self.preco_uma_casa = preco_uma_casa
        self.preco_duas_casas = preco_duas_casas
        self.preco_tres_casas = preco_tres_casas
        self.preco_quatro_casas = preco_quatro_casas
        self.preco_hotel = preco_hotel
        self.preco_construir = preco_construir
        self.preco_hipoteca = preco_hipoteca
        self.hipotecada = hipotecada
        self.dono = dono
        self.regiao = regiao

    def set_hipotecada(self, status_hipoteca):
        self.hipotecada = status_hipoteca

    def get_hipoteca(self):
        return self.hipotecada

    def get_dono(self):
        return self.dono

    def set_dono(self, dono_card):
        self.dono = dono_card


class card_player:

    propriedades = []

    def __init__(self, nome_player, tot_valores, local_atual, local_anterior, propriedade):
        self.nome_player = nome_player
        self.tot_valores = tot_valores
        self.local_atual = local_atual
        self.local_anterior = local_anterior
        self.propriedade = propriedade

    def get_player(self):
        return self.nome_player

    def set_nome_player(self, new_nome_player):
        self.nome_player = new_nome_player

    def get_tot_valores(self):
        return self.tot_valores

    def set_tot_valores(self, atualiza_tot_valores):
        self.tot_valores = atualiza_tot_valores

    def propriedade(self):
        self.__class__.propriedades.append(self)

    def get_propriedades(self):
        return self.__class__.propriedades




class User:
    seq = 0
    object = []

    def __init__(self, nome_player, tot_valores, local_atual, local_anterior, propriedade):
        self.id = None
        self.nome_player = nome_player
        self.tot_valores = tot_valores
        self.local_atual = local_atual
        self.local_anterior = local_anterior
        self.propriedade = propriedade

    def save(self):
        self.__class__.seq += 1
        self.id = self.__class__.seq
        self.__class__.object.append(self)

    def __str__(self):
        return self.nome_player

    def __repr__(self):
        return '<{}: {} - {} - {} - {} - {} - {}>\n'.format(self.__class__.__name__, self.id, self.nome_player, self.tot_valores, self.local_atual, self.local_anterior, self.propriedade)

    @classmethod
    def all(cls):
        return cls.object


if __name__ == '__main__':
    u1 = User('Regis', 35)
    u1.save()
    u2 = User('Fabio', 20)
    u2.save()
    print(User.all())


def card_noticias(self):
    from random import choice
    cards = []
    select = choice(cards)
    return str(select)