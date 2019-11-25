from mdp import Mdp
from parser_mdp import Parser

navigationFile = open("DeterministicGoalState/navigation_10.net")

navigationFileReaded = navigationFile.read()

navigationFileParsed = Parser(navigationFileReaded)

states = navigationFileParsed.get_states()

policy_lao, time_lao = Mdp(states).lao_star()

policy_iteration, time_iteration = Mdp(states).value_iteration()


print(time_lao)
print(time_iteration)
