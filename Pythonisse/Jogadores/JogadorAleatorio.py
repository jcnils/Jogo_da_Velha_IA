"""Jogo da Velha implementado em Python para o canal do youtube Jogando com Nils

Esta classe representa o jogador aleatorio, ela sempre joga em uma posicao disponivel.
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

import random
from ..Jogo.Jogador import Jogador

class JogadorAleatorio(Jogador):
    """Jogador Aleatorio joga em qualquer lugar livre"""

    def __init__(self, nome):
        self.nome = nome

    def pega_nome(self):
        return self.nome

    def jogada(self, tabuleiro, cor_da_peca):

        jogadas = list(range(0, 9))

        for jogada in jogadas:
            par_jogada = self.parse_jogada(jogada)
            if tabuleiro[par_jogada[0]][par_jogada[1]] != ' ':
                jogadas.remove(jogada)

        return self.parse_jogada(random.choice(jogadas))

    def parse_jogada(self, jogada):
        """retorna ponto da jogada"""
        pos = jogada

        ponto = (pos // 3, pos % 3)

        return ponto
