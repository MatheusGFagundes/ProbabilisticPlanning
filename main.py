from mdp import Mdp
from parser_mdp import Parser

navigationFile = open("RandomGoalState/navigation_1.net")

navigationFileReaded = navigationFile.read()

navigationFileParsed = Parser(navigationFileReaded)

states = navigationFileParsed.get_states()

Mdp(states).value_iteration()

exit(0)
