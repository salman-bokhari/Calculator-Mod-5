class CalculatorMemento:
    def __init__(self, state=None):
        self.state = state or {}

class Caretaker:
    def __init__(self):
        self.history = []

    def save(self, state):
        self.history.append(CalculatorMemento(state.copy()))

    def undo(self):
        if self.history:
            return self.history.pop().state
        return {}
