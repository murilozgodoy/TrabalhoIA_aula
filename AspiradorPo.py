from aigyminsper.search.search_algorithms import BuscaLargura, BuscaProfundidade
from aigyminsper.search.graph import State

class AspiradorPo(State):
    # op é a operacao que o agente usou para chegar no estado que ele esta
    def __init__(self, op, posicao_robo, condicao_esq, condicao_dir):
        # voce sempre deve usar esta chamada para inicializar a superclasse
        super().__init__(op)
        # posicao_robo = esq ou dir
        self.posicao_robo = posicao_robo
        # condicao_esq = sujo ou limpo
        self.condicao_esq = condicao_esq
        # condicao_dir = sujo ou limpo
        self.condicao_dir = condicao_dir

    def successors(self):
        # lista de objetos da classe AspiradorPo
        successors = []

        # ir p/ esq
        successors.append(AspiradorPo('ir p/ esq', 'esq', self.condicao_esq, self.condicao_dir)) 
        # ir p/ dir
        successors.append(AspiradorPo('ir p/ dir', 'dir', self.condicao_esq, self.condicao_dir)) # self serve para manter a posicao que ele estava antes dessa acao

        # limpar
        if self.posicao_robo == 'esq':
            successors.append(AspiradorPo('limpar', self.posicao_robo, 'limpo', self.condicao_dir))
        if self.posicao_robo == 'dir':
            successors.append(AspiradorPo('limpar', self.posicao_robo, self.condicao_esq, 'limpo'))

        return successors
    
    def is_goal(self):
        return self.condicao_esq == 'limpo' and self.condicao_dir == 'limpo'
    
    
    def description(self):
        return "Problema do aspirador de pó de 2 quartos"
    
    def cost(self): # mostra o custo de cada acao, e como limpar, ir para dir e esq tem o mesmo custo, sempre eh 1
        return 1
    
    def env(self):
        #
        # IMPORTANTE: este método não deve apenas retornar uma descrição do environment, mas 
        # deve também retornar um valor que descreva aquele nodo em específico. Pois 
        # esta representação é utilizada para verificar se um nodo deve ou ser adicionado 
        # na lista de abertos.
        #
        # Exemplos de especificações adequadas: 
        # - para o problema do soma 1 e 2: return str(self.number)+"#"+str(self.cost)
        # - para o problema das cidades: return self.city+"#"+str(self.cost())
        #
        # Exemplos de especificações NÃO adequadas: 
        # - para o problema do soma 1 e 2: return str(self.number)
        # - para o problema das cidades: return self.city
        #
        None

def main():
    estado_inicial = AspiradorPo('', 'esq', 'sujo', 'sujo') # como o agente nao fez nenhuma operacao ainda, deixar vazio
    algorithm = BuscaLargura()
    result = algorithm.search(estado_inicial) # sabe todo o caminho, pensando como se fosse uma arvore genealogica
    if result != None:
        print('Achou!')
        print(result.show_path()) # caminho da 'arvore genealogica' ate onde quer chegar
    else:
        print('Nao achou solucao')

if __name__ == '__main__':
    main()

# busca largura basicamente faz isso:
# function BuscaLargura(nodo_inicial):
    # Fila abertos
    # abertos.append(inicial)
    # while abertos.size > 0:
    #   m = abertos.remove()
    #   if n.is.goal():
    #       return n
    #   abertos.append(n.successors())
