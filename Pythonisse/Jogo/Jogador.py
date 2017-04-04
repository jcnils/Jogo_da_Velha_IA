"""Jogo da Velha implementado em Python para o canal do youtube Jogando com Nils

Esta classe representa a interface do tipo de jogador (interface de classe).

Todo:
    * terminar docstring
    * metodos da classe
"""

__author__ = "Nils"
__copyright__ = "Copyright 2017, Jogo da Velha JcN"
__credits__ = ["Nils"]
__license__ = "GNU GENERAL PUBLIC LICENSE"
__maintainer__ = "Nils"


class Jogador:
    """ Interface do Jogador para ser utilizada pelo Jogo da Velha """


    def pega_nome(self):
        """Retorna o nome do Jogador"""
        raise NotImplementedError

    def jogada(self, tabuleiro, cor_da_peca):
        """ Retorna a jogada do jogodor """
        raise NotImplementedError
