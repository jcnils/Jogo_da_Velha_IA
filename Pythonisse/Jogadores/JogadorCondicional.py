"""Jogo da Velha implementado em Python para o canal do youtube Jogando com Nils

Esta classe representa o jogador condicional, conforme as aulas da live ele usa base de conhecimento
para as primeiras jogadas, depois verifica condições de derrota ou vitória.
Instancia de Jogador.py

Todo:
    * terminar docstring
    * metodos da classe
"""

__author__ = "Nils"
__copyright__ = "Copyright 2017, Jogo da Velha JcN"
__credits__ = ["Nils"]
__license__ = "GNU GENERAL PUBLIC LICENSE"
__maintainer__ = "Nils"

from ..Jogo.Jogador import Jogador

class JogadorCondicional(Jogador):
    """Jogador Condicional com base de conhecimento"""

    def __init__(self, nome):
        self.nome = nome

    def pega_nome(self):
        return self.nome

    def jogada(self, tabuleiro, cor_da_peca):

        turno = verifica_turno(tabuleiro)
        jogada = 7
        peca_adversario = (cor_da_peca+1)%2


        if turno == 1:
            jogada = 7
        elif turno == 2:
            if tabuleiro[1][1] == peca_adversario:
                jogada = 7
            else:
                jogada = 5
        elif turno == 3:
            if tabuleiro[1][1] == peca_adversario:
                jogada = 3
            elif tabuleiro[0][1] == peca_adversario or tabuleiro[1][0] == peca_adversario:
                jogada = 9
            elif tabuleiro[1][2] == peca_adversario or tabuleiro[2][1] == peca_adversario:
                jogada = 1
            elif tabuleiro[0][2] == peca_adversario:
                jogada = 1
            else:
                #jogou no 1 ou no 9
                jogada = 3
        else:

            jogada = condicao_vitoria(tabuleiro, cor_da_peca)

            if jogada == 0:
                jogada = codicao_derrota(tabuleiro, peca_adversario)

                if jogada == 0:
                     
                

        return self.parse_jogada(jogada)



    def condicao_vitoria(self, tabuleiro,cor_da_peca):
        """ retorna a jogada vencedora, senao retorna 0 """

        pass

    
    def condicao_derrota(self, parameter_list,peca_adversario):
        """ retorna bloqueio de derrota do adversario, senao retorna 0 """
        pass

    def verifica_turno(self, tabuleiro):
        pass
    
    def parse_jogada(self, jogada):
        """retorna ponto da jogada"""
        pos = jogada - 1

        ponto = (pos // 3  , pos % 3)

        return ponto
        