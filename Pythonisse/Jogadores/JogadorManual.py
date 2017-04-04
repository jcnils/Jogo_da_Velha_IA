"""Jogo da Velha implementado em Python para o canal do youtube Jogando com Nils

Esta classe representa o jogador manual, ela pega input do teclado.
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

class JogadorManual(Jogador):
    """Jogador Manual recebe input do teclado para cada jogada"""

    def __init__(self, nome):
        self.nome = nome

    def pega_nome(self):
        return self.nome

    def jogada(self, tabuleiro, cor_da_peca):

        jogada = int(input(self.pega_nome() + ", cor - " + str(cor_da_peca) +
                            " escolha tua jogada: (1-9) "))
        while jogada not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            jogada = int(input("Jogada Invalida, tente novamente"))

        return self.parse_jogada(jogada)

    def parse_jogada(self, jogada):
        """retorna ponto da jogada"""
        pos = jogada - 1

        ponto = (pos // 3  , pos % 3)

        return ponto
        