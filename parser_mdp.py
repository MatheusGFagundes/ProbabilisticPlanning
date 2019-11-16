from elements import Variant, Action, State
import re

class Parser:
    def __init__(self, txt_file):
        self.txt = txt_file
        states = self.get_all_states()
        actions_def = self.get_all_action()
        costs = self.get_all_cost(actions_def)
        
        for action_name, state_name  in costs.keys():
            new_action = Action(action_name)
            if(not states[state_name].is_goal):
                new_action.add_cost(float(costs[action_name, state_name]["cost"]))
                for variant in costs[action_name, state_name]["variants"]:
                    new_action.add_variant(Variant(states[variant["to"]], float(variant["prob"])))
                states[state_name].add_action(new_action)
        self.states = states
        

    def get_states(self):
        return self.states
  
    def get_all_states(self):
        states_text = re.findall('^states(.*?)^endstates',self.txt,re.DOTALL|re.MULTILINE)[0]
        allStates = re.findall("robot-at-x[0-9]*y[0-9]*", states_text)
        
        state_inital_text = re.findall('^initialstate(.*?)^endinitialstate',self.txt,re.DOTALL|re.MULTILINE)[0]
        state_inital_name = re.findall("robot-at-x[0-9]*y[0-9]*", state_inital_text)[0]
        
        state_goal_text = re.findall('^goalstate(.*?)^endgoalstate',self.txt,re.DOTALL|re.MULTILINE)[0]
        state_goal_name = re.findall("robot-at-x[0-9]*y[0-9]*", state_goal_text)[0]
        states = {}
        for state_name in allStates:
            is_initial = state_inital_name == state_name
            is_goal = state_goal_name == state_name
            states[state_name] = State(state_name, is_initial, is_goal)
        return states


    def get_all_action(self):
        all_actions = re.findall("action [a-z-A-Z]*", self.txt )
        actions_def = {}
        for action_name in all_actions:
            current_action = re.findall("^{action_name}(.*?)^endaction".format(action_name = action_name),self.txt,re.DOTALL|re.MULTILINE)[0]
            actions = re.findall("robot-at-x[0-9]*y[0-9]* robot-at-x[0-9]*y[0-9]* [0-9]*.[0-9]* [0-9]*.[0-9]*", current_action)
            
            for index in range(len(actions)):
                name = action_name.split()[1]
                split_values = actions[index].split()
                if((name, split_values[0]) not in actions_def):
                     actions_def[(name, split_values[0])] = []
                actions_def[(name, split_values[0])].append({"to":split_values[1], "prob":split_values[2]})
        return actions_def 


    def get_all_cost(self,actions_def):
        cost_section =  re.findall("^cost(.*?)^endcost",self.txt,re.DOTALL|re.MULTILINE)[0]
        costs = re.findall("robot-at-x[0-9]*y[0-9]* [a-z-,A-Z]* [0-9]*.[0-9]*", cost_section)
        for cost in costs:
            split_values = cost.split()
            variants = actions_def[(split_values[1],split_values[0])]
            actions_def[(split_values[1],split_values[0])] = {"cost":split_values[2] , "variants": variants }
        return actions_def  
    

    
   

    