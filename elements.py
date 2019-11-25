class Variant:
    def __init__(self, next_state, prob):
        self.next_state = next_state
        self.prob = prob


class Action:
    def __init__(self, name):
        self.name = name
        self.variants = []

    def add_cost(self, cost):
        self.cost = cost

    def add_variant(self, variant):
        self.variants.append(variant)


class State:
    def __init__(self, name, is_inital, is_goal):
        self.name = name
        self.x = int(self.name.split("x")[1].split("y")[0])
        self.y = int(self.name.split("y")[1])
        self.is_inital = is_inital
        self.is_goal = is_goal
        self.actions = []
        self.chosen_action = ""
        self.value = 0
        self.predecessors = []

    def add_action(self, action):
        self.actions.append(action)

    def update_values(self):
        if (self.is_goal):
            self.value = 0
            return self.value

        old_value = self.value
        actions_value = map(lambda x: self.calculate_action_value(x), self.actions)
        min_action = min(list(actions_value), key=lambda x: x[1])
        self.value = min_action[1]
        self.chosen_action = min_action[0]
        return abs(old_value - self.value)

    def calculate_action_value(self, action):
        value = 0
        for variant in action.variants:
            value += variant.prob * (variant.next_state.value + action.cost)

        return action, value
