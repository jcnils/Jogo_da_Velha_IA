"""Jogo da Velha implementado em Python para o canal do youtube Jogando com Nils

Esta classe estrutura um jogo da velha entre dois jogadores, para isso os jogadores
devem ser definidos a partir da classe jogador.

Todo:
    * terminar docstring
    * metodos da classe
"""

__author__ = "Nils"
__copyright__ = "Copyright 2017, Jogo da Velha JcN"
__credits__ = ["Nils"]
__license__ = "GNU GENERAL PUBLIC LICENSE"
__version__ = "0.0.1"
__maintainer__ = "Nils"
__email__ = ""
__status__ = "Production"


class JogoDaVelha:
	"""Esta classe estrutura um jogo da velha entre dois jogadores"""

	def __init__(self, jogador1, jogador2):
		self.vencedor = 2 # 2 significa empate / 2 means draw

		self.tabuleiro = [
			[' ', ' ', ' '],
			[' ', ' ', ' '],
			[' ', ' ', ' '],
		]

		self.jogadores = []
		self.jogadores.append(jogador1)
		self.jogadores.append(jogador2)

		self.jogador_da_vez = 0

		#mensagems
		self.formato_tabuleiro = '''
			\t| %s | %s | %s |
			\t-------------
			\t| %s | %s | %s |
			\t-------------
			\t| %s | %s | %s |'''

		self.mensagem_jogada = """\t %s jogou."""

		self.mensagem_vencedor = """\t %s venceu o jogo, %s perdeu"""

		self.mensagem_empate = """\t %s empatou com %s """

		self.mensagem_jogadainvalida = """Jogada invalida"""

	def altera_tabuleiro(self, jogada, jogador):
		"""Altera tabuleiro com a jogada """
		if self.tabuleiro[jogada[0]][jogada[1]] == ' ':
			self.tabuleiro[jogada[0]][jogada[1]] = jogador
			return True

		return False

	def imprime_tabuleiro(self, inicio=None):
		"""Mostra situacao atual do tabuleiro """
		if inicio is None:
			#Mostra tabuleiro na tela
			print(self.formato_tabuleiro % tuple(self.tabuleiro[0] + self.tabuleiro[1] + self.tabuleiro[2]))
		else:
			print(self.formato_tabuleiro % (1, 2, 3, 4, 5, 6, 7, 8, 9))

		print()

	def roda_partida(self):
		"""Loop da partida"""
		andamento = True
		jogada = 0
		contador_jogadas = 0
		self.jogador_da_vez = 0
		print("""Jogadas possiveis""")
		self.imprime_tabuleiro(1)
		print()

		while andamento:

			#Pega a jogada e altera tabuleiro se valida
			jogada = self.jogadores[self.jogador_da_vez].jogada(self.tabuleiro, self.jogador_da_vez)

			if not self.altera_tabuleiro(jogada, self.jogador_da_vez):
				#se nao jogada alterou tabuleiro acaba aqui e sai do loop
				print(self.mensagem_jogadainvalida)
				self.vencedor = (self.jogador_da_vez+1)%2
				andamento = False


			contador_jogadas += 1


			#Imprime tabuleiro e jogador
			print(self.mensagem_jogada % self.jogadores[self.jogador_da_vez].pega_nome())
			self.imprime_tabuleiro()


			#Verifica fim da partida Imprime resultado e sai do loop em condicao de encerramento.
			if self.venceu(jogada):
				self.vencedor = self.jogador_da_vez
				andamento = False
			elif contador_jogadas == 9:
				#acabaram espacos para jogar
				self.vencedor = 2 #empate
				andamento = False

			self.jogador_da_vez = (self.jogador_da_vez+1)%2


		self.resultado()


	def venceu(self, jogada):
		"""verifica se jogador venceu o jogo"""
		cordx = jogada[0]
		cordy = jogada[1]

		#verifica vertical no Y da ultima jogada
		if self.tabuleiro[0][cordy] == self.tabuleiro[1][cordy] == self.tabuleiro[2][cordy]:
			return True

		#verifica horizontal no X da ultima jogada
		if self.tabuleiro[cordx][0] == self.tabuleiro[cordx][1] == self.tabuleiro[cordx][2]:
			return True

		#verifica diagonal
		if cordx == cordy and self.tabuleiro[0][0] == self.tabuleiro[1][1] == self.tabuleiro[2][2]:
			return True

		#verifica diagonal inversa
		if cordx + cordy == 2 and self.tabuleiro[0][2] == self.tabuleiro[1][1] == self.tabuleiro[2][0]:
			return True

		return False


	def resultado(self):
		""" imprime resultado da partida"""



		if self.vencedor == 2:
			#empate
			print(self.mensagem_empate %
					(self.jogadores[self.jogador_da_vez].pega_nome(),
					 self.jogadores[(self.jogador_da_vez+1)%2].pega_nome())
				)

		else:
			#vitoria
			print(self.mensagem_vencedor %
					(self.jogadores[self.vencedor].pega_nome(),
					self.jogadores[(self.vencedor+1)%2].pega_nome())
				)
