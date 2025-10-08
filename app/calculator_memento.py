class CalculatorMemento:
    def __init__(self, state):
        self.state = state

class Caretaker:
    def __init__(self):
        self.history = []

    def save(self, state):
        self.history.append(CalculatorMemento(state))

    def undo(self):
        if self.history:
            return self.history.pop().state
        return None
