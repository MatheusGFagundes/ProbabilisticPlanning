import time


class Mdp:
    def __init__(self, states):
        self.states = states

    def value_iteration(self, epsilon=0.01):
        start_time = time.time()
        min_residual = 1000000000000000
        count = 0
        while min_residual > epsilon:
            count += 1
            all_residual = list(map(lambda x: x.update_values(), list(self.states.values())))
            min_residual = max(all_residual)

        print("--- it took %s seconds---" % (time.time() - start_time))
        print("policy pi", count)
        print("     State    ", "    action  ", "         value  ")
        print("------------------------------------------")
        for state in list(self.states.values()):
            try:
                print(state.name, " ", state.chosen_action.name, " ", state.value)
            except:
                print(state.name, "goal_state", 0)

    def laoStar(self, epsilon=0.01):
        start_time = time.time()
        min_residual = 1000000000000000
        count = 0

# - O grafo G' inicialmente consiste no estado inicial s
#
# - Enquanto o melhor grafo possui estados folha nao-terminais:
# 	- Expanda a melhor solucao parcial:
# 		- Expanda um estado folha nao-terminal n do grafo da melhor solucao parcial
#
# 		- Adicione quaisquer novos sucessores ao grafo G'.
#
# 		- Para cada novo estado i adicionado a G' por expandir n
# 			- Se i eh um estado meta, entao f(i) = 0
# 			- Se nao, f(i) = h(i) (custo da heuristica)
#
# 	- Atualize os custos dos estados e marque as melhores acoes:
# 		- Crie um conjunto Z que contem os estados expandidos e inclua os estados ancestrais pelos quais o estado expandido pode ser atingindo ao seguir a melhor solucao //Sera que isso eh como um plano parcial?
# 		- Utilize o algoritmo de iteracao de valor nos estados do conjunto Z para atualizar os custos e determinar a melhor acao para cada estado
#
# - Teste de convergencia:
# 	- se uma iteracao de politica foi utilizada, retorne a solucal otima do grafo
#
# 	- se uma iteracao de valores foi utilizada, utilize-a novamente nos estados do grafo de melhor solucao e continue ate que uma das condicoes abaixo seja satisfeita:
# 		- se o error ficar menor que err, retorne a solucao
# 		- se a melhor solucao do grafo atual mudar ate que chegue a um estado folha nao expandido, retorne ao segundo passo
#
#
# LAO*(grafo):
# 	while(bestG.tipState == nonTerminal && !converged):
# 		expandPartialSolution()
# 		updateStateCosts() //update state costs and mark best actions
# 		converged = convergenceTest()
#
# 	return bestG
#
# expandPartialSolution(g):
# 	for newNodes in G
