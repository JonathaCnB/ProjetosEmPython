from lib import *
from ProjetoBancoImobiliario.libs.cards import *
from random import randint
propriedade = list()

cardInicial = {'Preço': 2000, 'Dono': 'Bonus'}
propriedade.append(cardInicial)
card9deJulho = {'Preço': 1000, 'Aluguel': 60, 'Com1Casa': 300, 'Com2Casas': 900, 'Com3Casas': 2700, 'Com4Casas': 4000,
                'ComHotel': 5000, 'PreçoConstrução': 500, 'Hipoteca': 500, 'Hipotecada': False, 'Dono': 'Banco', 'Conjunto': 'Verde'}
propriedade.append(card9deJulho)
cardAvBrasil = {'Preço': 1000, 'Aluguel': 40, 'Com1Casa': 200, 'Com2Casas': 600, 'Com3Casas': 1800, 'Com4Casas': 3200,
                'ComHotel': 4500, 'PreçoConstrução': 500, 'Hipoteca': 500, 'Hipotecada': False, 'Dono': 'Banco', 'Conjunto': 'Verde'}
propriedade.append(cardAvBrasil)
cardAcBancoItau = {'Preço': 2000, 'Aluguel': 500, 'Hipoteca': 1000, 'Hipotecada': False, 'Dono': 'Banco', 'Conjunto': 'Ações'}
propriedade.append(cardAcBancoItau)
cardAvBeiraMar = {'Preço': 1000, 'Aluguel': 20, 'Com1Casa': 100, 'Com2Casas': 300, 'Com3Casas': 900, 'Com4Casas': 1600,
                  'ComHotel': 2500, 'PreçoConstrução': 500, 'Hipoteca': 500, 'Hipotecada': False, 'Dono': 'Banco', 'Conjunto': 'Verde'}
propriedade.append(cardAvBeiraMar)
cardAvRioBranco = {'Preço': 2400, 'Aluguel': 200, 'Com1Casa': 1000, 'Com2Casas': 3000, 'Com3Casas': 7500, 'Com4Casas': 9250,
                   'ComHotel': 11000, 'PreçoConstrução': 1500, 'Hipoteca': 1200, 'Hipotecada': False, 'Dono': 'Banco', 'Conjunto': 'Vermelho'}
propriedade.append(cardAvRioBranco)
cardNoticias = {'Preço': 2400, 'Hipotecada': False, 'Dono': 'Banco', 'Conjunto': 'Bonus'}
propriedade.append(cardNoticias)
cardAvdoEstado = {'Preço': 2200, 'Aluguel': 180, 'Com1Casa': 900, 'Com2Casas': 2500, 'Com3Casas': 7000, 'Com4Casas': 8750,
                  'ComHotel': 10500, 'PreçoConstrução': 1500, 'Hipoteca': 1100, 'Hipotecada': False, 'Dono': 'Banco', 'Conjunto': 'Vermelho'}
propriedade.append(cardAvdoEstado)
cardAcTamViagens = {'Preço': 2000, 'Aluguel': 500, 'Hipoteca': 1000, 'Hipotecada': False, 'Dono': 'Banco', 'Conjunto': 'Ações'}
propriedade.append(cardAcTamViagens)
cardAvdoContorno = {'Preço': 2200, 'Aluguel': 180, 'Com1Casa': 900, 'Com2Casas': 2500, 'Com3Casas': 7000, 'Com4Casas': 8750,
                    'ComHotel': 10500, 'PreçoConstrução': 1500, 'Hipoteca': 1100, 'Hipotecada': False, 'Dono': 'Banco', 'Conjunto': 'Vermelho'}
propriedade.append(cardAvdoContorno)
cardParadaLivre = {'Preço': 0, 'Aluguel': 0, 'Hipoteca': 0, 'Hipotecada': False, 'Dono': 'Banco', 'Conjunto': 'Bonus'}
propriedade.append(cardParadaLivre)
cardNoticias2 = {'Preço': 2400, 'Hipotecada': False, 'Dono': 'Banco', 'Conjunto': 'Bonus'}
propriedade.append(cardNoticias2)
cardAvReboucas = {'Preço': 2000, 'Aluguel': 160, 'Com1Casa': 800, 'Com2Casas': 2200, 'Com3Casas': 6000, 'Com4Casas': 8000,
                  'ComHotel': 10000, 'PreçoConstrução': 1000, 'Hipoteca': 1000, 'Hipotecada': False, 'Dono': 'Banco', 'Conjunto': 'Azul'}
propriedade.append(cardAvReboucas)
cardAvSantoAmaro = {'Preço': 2000, 'Aluguel': 140, 'Com1Casa': 700, 'Com2Casas': 2000, 'Com3Casas': 5500, 'Com4Casas': 7500,
                    'ComHotel': 9500, 'PreçoConstrução': 1000, 'Hipoteca': 1000, 'Hipotecada': False, 'Dono': 'Banco', 'Conjunto': 'Azul'}
propriedade.append(cardAvSantoAmaro)
cardAcPostoIpiranga = {'Preço': 2000, 'Aluguel': 500, 'Hipoteca': 1000, 'Hipotecada': False, 'Dono': 'Banco', 'Conjunto': 'Ações'}
propriedade.append(cardAcPostoIpiranga)
cardRuadaConsolacao = {'Preço': 2000, 'Aluguel': 140, 'Com1Casa': 700, 'Com2Casas': 2000, 'Com3Casas': 5500, 'Com4Casas': 7500,
                       'ComHotel': 9500, 'PreçoConstrução': 1000, 'Hipoteca': 1000, 'Hipotecada': False, 'Dono': 'Banco', 'Conjunto': 'Azul'}
propriedade.append(cardRuadaConsolacao)
cardSorte = {'Preço': 2000, 'Hipotecada': False, 'Dono': 'Banco', 'Conjunto': 'Bonus'}
propriedade.append(cardSorte)
cardMorumbi = {'Preço': 4000, 'Aluguel': 500, 'Com1Casa': 2000, 'Com2Casas': 6000, 'Com3Casas': 14000, 'Com4Casas': 17000,
               'ComHotel': 20000, 'PreçoConstrução': 2000, 'Hipoteca': 2000, 'Hipotecada': False, 'Dono': 'Banco', 'Conjunto': 'Rosa'}
propriedade.append(cardMorumbi)
cardHigienopolis = {'Preço': 3500, 'Aluguel': 350, 'Com1Casa': 1750, 'Com2Casas': 5000, 'Com3Casas': 11000, 'Com4Casas': 13000,
                    'ComHotel': 15000, 'PreçoConstrução': 2000, 'Hipoteca': 1750, 'Hipotecada': False, 'Dono': 'Banco', 'Conjunto': 'Rosa'}
propriedade.append(cardHigienopolis)
cardAvSaoJoao = {'Preço': 1200, 'Aluguel': 80, 'Com1Casa': 400, 'Com2Casas': 1000, 'Com3Casas': 3000, 'Com4Casas': 4500,
                 'ComHotel': 6000, 'PreçoConstrução': 500, 'Hipoteca': 600, 'Hipotecada': False, 'Dono': 'Banco', 'Conjunto': 'Lilas'}
propriedade.append(cardAvSaoJoao)
cardFeriado = {'Preço': 0, 'Aluguel': 0, 'Hipoteca': 0, 'Hipotecada': False, 'Dono': 'Banco', 'Conjunto': 'Bonus'}
propriedade.append(cardFeriado)
cardAvIpiranga = {'Preço': 1000, 'Aluguel': 60, 'Com1Casa': 300, 'Com2Casas': 900, 'Com3Casas': 2700, 'Com4Casas': 4000,
                  'ComHotel': 5000, 'PreçoConstrução': 500, 'Hipoteca': 600, 'Hipotecada': False, 'Dono': 'Banco', 'Conjunto': 'Lilas'}
propriedade.append(cardAvIpiranga)
cardAcNivea = {'Preço': 2000, 'Aluguel': 500, 'Hipoteca': 1000, 'Hipotecada': False, 'Dono': 'Banco', 'Conjunto': 'Ações'}
propriedade.append(cardAcNivea)
cardReves = {'Preço': 2000, 'Hipotecada': False, 'Dono': 'Banco', 'Conjunto': 'Bonus'}
propriedade.append(cardReves)
cardNoticias3 = {'Preço': 2400, 'Hipotecada': False, 'Dono': 'Banco', 'Conjunto': 'Bonus'}
propriedade.append(cardNoticias3)
cardRBrigadeiroFLima = {'Preço': 1400, 'Aluguel': 100, 'Com1Casa': 500, 'Com2Casas': 1500, 'Com3Casas': 4500, 'Com4Casas': 6250,
                        'ComHotel': 7500, 'PreçoConstrução': 1000, 'Hipoteca': 700, 'Hipotecada': False, 'Dono': 'Banco', 'Conjunto': 'Azul'}
propriedade.append(cardRBrigadeiroFLima)
cardAvRecife = {'Preço': 1400, 'Aluguel': 100, 'Com1Casa': 500, 'Com2Casas': 1500, 'Com3Casas': 4500, 'Com4Casas': 6250,
                'ComHotel': 7500, 'PreçoConstrução': 1000, 'Hipoteca': 700, 'Hipotecada': False, 'Dono': 'Banco', 'Conjunto': 'Azul'}
propriedade.append(cardAvRecife)
cardNoticias4 = {'Preço': 2400, 'Hipotecada': False, 'Dono': 'Banco', 'Conjunto': 'Bonus'}
propriedade.append(cardNoticias4)
cardAvPaulista = {'Preço': 1600, 'Aluguel': 120, 'Com1Casa': 600, 'Com2Casas': 1800, 'Com3Casas': 5000, 'Com4Casas': 7000,
                  'ComHotel': 9000, 'PreçoConstrução': 1000, 'Hipoteca': 800, 'Hipotecada': False, 'Dono': 'Banco', 'Conjunto': 'Azul'}
propriedade.append(cardAvPaulista)
cardAcVivo = {'Preço': 2000, 'Aluguel': 500, 'Hipoteca': 1000, 'Hipotecada': False, 'Dono': 'Banco', 'Conjunto': 'Ações'}
propriedade.append(cardAcVivo)
cardPrisao = {'Preço': 0, 'Aluguel': 0, 'Hipoteca': 0, 'Hipotecada': False, 'Dono': 'Banco', 'Conjunto': 'Bonus'}
propriedade.append(cardPrisao)
cardAvJKubitschek = {'Preço': 3200, 'Aluguel': 280, 'Com1Casa': 1500, 'Com2Casas': 4500, 'Com3Casas': 10000, 'Com4Casas': 12000,
                     'ComHotel': 14000, 'PreçoConstrução': 2000, 'Hipoteca': 1600, 'Hipotecada': False, 'Dono': 'Banco', 'Conjunto': 'Laranja'}
propriedade.append(cardAvJKubitschek)
cardNoticias5 = {'Preço': 2400, 'Hipotecada': False, 'Dono': 'Banco', 'Conjunto': 'Bonus'}
propriedade.append(cardNoticias5)
cardROscarFreire = {'Preço': 3000, 'Aluguel': 260, 'Com1Casa': 1300, 'Com2Casas': 3900, 'Com3Casas': 9000, 'Com4Casas': 11000,
                    'ComHotel': 12750, 'PreçoConstrução': 2000, 'Hipoteca': 1500, 'Hipotecada': False, 'Dono': 'Banco', 'Conjunto': 'Laranja'}
propriedade.append(cardROscarFreire)
cardIbirapuera = {'Preço': 3000, 'Aluguel': 260, 'Com1Casa': 1300, 'Com2Casas': 3900, 'Com3Casas': 9000, 'Com4Casas': 11000,
                  'ComHotel': 12750, 'PreçoConstrução': 2000, 'Hipoteca': 1500, 'Hipotecada': False, 'Dono': 'Banco', 'Conjunto': 'Laranja'}
propriedade.append(cardIbirapuera)
cardVieiraSouto = {'Preço': 2800, 'Aluguel': 260, 'Com1Casa': 1300, 'Com2Casas': 3600, 'Com3Casas': 8500, 'Com4Casas': 10250,
                   'ComHotel': 12000, 'PreçoConstrução': 1500, 'Hipoteca': 1400, 'Hipotecada': False, 'Dono': 'Banco', 'Conjunto': 'Amarelo'}
propriedade.append(cardVieiraSouto)
cardAcFIAT = {'Preço': 2000, 'Aluguel': 500, 'Hipoteca': 1000, 'Hipotecada': False, 'Dono': 'Banco', 'Conjunto': 'Ações'}
propriedade.append(cardAcFIAT)
cardPresVargas = {'Preço': 2600, 'Aluguel': 220, 'Com1Casa': 1100, 'Com2Casas': 3300, 'Com3Casas': 8000, 'Com4Casas': 9750,
                   'ComHotel': 11500, 'PreçoConstrução': 1500, 'Hipoteca': 1300, 'Hipotecada': False, 'Dono': 'Banco', 'Conjunto': 'Amarelo'}
propriedade.append(cardPresVargas)
cardNoticias6 = {'Preço': 2400, 'Hipotecada': False, 'Dono': 'Banco', 'Conjunto': 'Bonus'}
propriedade.append(cardNoticias6)
cardNiemeyer = {'Preço': 2600, 'Aluguel': 220, 'Com1Casa': 1100, 'Com2Casas': 3300, 'Com3Casas': 8000, 'Com4Casas': 9750,
                   'ComHotel': 11500, 'PreçoConstrução': 1500, 'Hipoteca': 1300, 'Hipotecada': False, 'Dono': 'Banco', 'Conjunto': 'Amarelo'}
propriedade.append(cardNiemeyer)

print(cardNiemeyer.get('Preço'))


card_leblon = card_titulo_posse(100, 6, 30, 90, 270, 400, 500, 50, 50, False, 'Banco', 'Rosa')
card_nsa_copacabana = card_titulo_posse(100, 4, 20, 60, 180, 320, 450, 50, 50, False, 'Banco', 'Rosa')
tot_tabuleiro = 0
dadosiguais = 0
turn_on = True
while turn_on is True:
    if dadosiguais == 3:
        turn_on = False
    dado0 = randint(1, 6)
    dado1 = randint(1, 6)
    tot_jogada = dado0 + dado1
    tot_tabuleiro += tot_jogada
    if tot_tabuleiro >= 39:
        tot_tabuleiro = tot_tabuleiro - 39
    if dado0 == dado1:
        dadosiguais += 1
    if str(tot_tabuleiro) in '0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39':
        if propriedade[tot_tabuleiro]['Dono'] == 'Banco':
            compra = str(input('propriedade sem dono deseja comprar? '))
            if compra in 'sS':
                print(propriedade[tot_tabuleiro]['Preço'])
                propriedade[tot_tabuleiro]['Dono'] = 'Player'

            else:
                continue
    print(dado0, dado1, tot_jogada, tot_tabuleiro)

print(propriedade[0]['Dono'])

