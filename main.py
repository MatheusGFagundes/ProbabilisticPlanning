# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 17:45:10 2019

@author: mgmat
"""

from parser_mdp import Parser
from mdp import Mdp
from functools import reduce
f = open("RandomGoalState/navigation_10.net")
file_txt = f.read()
parser = Parser(file_txt)
states = parser.get_states()

Mdp(states).value_iteration()

