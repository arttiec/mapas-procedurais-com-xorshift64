class Xorshift64:
    
    '''
    Classe que implemente o gerado de números pseudoaleatórios.

    Attributes:
        state (int): define o valor inicial do qual será o ponto de partida para gerar os outros números.

    Methods:
        xorshift() -> int: usa operações de deslocamento de bit para gerar números pseudoaleatório.
        Seu retorno é um número inteiro multiplicado por um fator constante para melhorar a distribuição aleatória.
    '''
    
    def __init__(self, state):
        self.state = state

    def xorshift64(self):
        self.state ^= self.state >> 21
        self.state ^= self.state << 45
        self.state ^= self.state >> 4

        return self.state * 0x2545F4914F6CDD1D