# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 17:40:38 2019

@author: mgmat
"""

import time

class Mdp:

    
    def __init__(self, states):
        self.states = states

    def value_iteration(self, epson =0.01):   
        from functools import reduce
        start_time = time.time()
        min_residual = 1000000000000000
        count = 0
        while min_residual > epson:
            count+=1
            all_residual = list(map(lambda x: x.update_values(), list(self.states.values())))
            min_residual =  max(all_residual)
        
        print("--- it took %s seconds---" % (time.time() - start_time))
        print("policy pi", count)
        print("     State    ", "    action  ", "         value  ")
        print("------------------------------------------")
        for state in list(self.states.values()): 
            try:
                 print(state.name, " ", state.chosen_action.name, " " ,state.value) 
            except:
                 print(state.name, "goal_state", 0)