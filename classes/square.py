class Square:
    def __init__(self, value):
        self.appearance = '.'
        self.value = value

    # Surement pas nécessaire
    def set_value(self, value):
        self.value = value

    def reveal_value(self):
        self.appearance = self.value
