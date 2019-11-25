import time


class Mdp:
    def __init__(self, states):
        self.states = states.values()

    def value_iteration(self, epsilon=0.01):
        start_time = time.time()
        max_residual = 1000000000000000
        count = 0
        response = []
        converge_time = 0
        while max_residual > epsilon:
            count += 1
            all_residual = list(map(lambda x: x.update_values(), list(self.states)))
            max_residual = max(all_residual)
        converge_time = (time.time() - start_time)
        response.append("--- it took %s seconds---" % (converge_time))
        response.append("policy pi" + str(count))
        response.append("     State    " + "    action  " + "    value  ")
        response.append("------------------------------------------")
        for state in list(self.states):
            try:
                response.append(state.name + " " + state.chosen_action.name + " " + str(state.value))
            except:
                 response.append(state.name + "goal_state 0")
        return "\n".join(response), converge_time

    
    def lao_star(self):
        start_time = time.time()
        response = []
        for state in self.states:
            if (state.is_inital):
                initial = state
            if (state.is_goal):
                goal = state
        
    
        initial.predecessors  = []
        visited_states = {initial}
        initial.value =  abs(initial.x - goal.x) + abs(initial.y - goal.y)


        while(True):
            current_best = sorted(visited_states, key = lambda x: x.value)[0]
            all_possible_next = []
            for acao in current_best.actions:
                for variant in acao.variants:
                    variant.next_state.value = max(abs(variant.next_state.x - goal.x) + abs(variant.next_state.y - goal.y),variant.next_state.value)
                    if(variant.next_state.name != current_best.name):
                        all_possible_next.append(variant.next_state)
            
            new_state = min(all_possible_next, key = lambda x: x.value)
            new_state.predecessors =   current_best.predecessors + [current_best]
            visited_states.add(new_state)
            if(new_state.is_goal):
                converge_time = (time.time() - start_time)
                response.append("--- it took %s seconds---" % (converge_time))
                response.append("     State    " + "    action  " + "    value  ")
                for state in new_state.predecessors:
                    try:
                        response.append(state.name + " " + state.chosen_action.name + " "  + str(state.value)) 
                    except:
                        response.append(state.name + "goal_state 0")
                return "\n".join(response), converge_time
            self.states = [new_state] + new_state.predecessors        
            self.value_iteration()
        
                    
            
        
            
            
        
