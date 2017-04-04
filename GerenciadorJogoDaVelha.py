"""Jogo da Velha implementado em Python para o canal do youtube Jogando com Nils

Esta classe representa o gerenciador de jogos da velha.

Todo:
    * terminar docstring
    * metodos da classe
"""

__author__ = "Nils"
__copyright__ = "Copyright 2017, Jogo da Velha JcN"
__credits__ = ["Nils"]
__license__ = "GNU GENERAL PUBLIC LICENSE"
__maintainer__ = "Nils"

from Pythonisse.Jogo.Jogador import Jogador
from Pythonisse.Jogo.JogoDaVelha import JogoDaVelha
from Pythonisse.Jogadores.JogadorManual import JogadorManual
from Pythonisse.Jogadores.JogadorAleatorio import JogadorAleatorio

class GerenciadorJogoDaVelha():
    """Gerencia os jogos que acontecerao, insira os jogadores na linha abaixo.
    ex:
    """

    #Atribui jogadores

    jogador1 = JogadorManual("Humano")
    jogador2 = JogadorAleatorio("Aleatorio")
    #jogador3 = JogadorIA_IF

    #Sequencia de jogos

    jogo1 = JogoDaVelha(jogador1, jogador2)
    jogo2 = JogoDaVelha(jogador2, jogador1)



    #Resultados


    jogo1.roda_partida()
    jogo2.roda_partida()