from mdp import Mdp
from parser_mdp import Parser
import glob

files = glob.glob('DeterministicGoalState/*') + glob.glob('RandomGoalState/*')

for file in files[11:12]:
    navigationFile = open(file)

    navigationFileReaded = navigationFile.read()

    navigationFileParsed = Parser(navigationFileReaded)

    states = navigationFileParsed.get_states()

    policy_lao, time_lao = Mdp(states).lao_star()

    print("LAO, " + file.split('\\')[0]+', '+ file.split('\\')[1] +", "+ str(round(time_lao,2)))
    
    policy_iteration, time_iteration = Mdp(states).value_iteration()
    
    print("ITER, " + file.split('\\')[0]+', '+ file.split('\\')[1] +", "+str(round(time_iteration,2)))