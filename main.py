from mdp import Mdp
from parser_mdp import Parser

navigationFile = open("RandomGoalState/navigation_10.net")

navigationFileReaded = navigationFile.read()

navigationFileParsed = Parser(navigationFileReaded)

states = navigationFileParsed.get_states()

Mdp(states).value_iteration()

Mdp(states).laoStar()
