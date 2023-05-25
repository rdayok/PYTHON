class AC:
    def __init__(self):
        self.is_on = False
        self.temperature = 16

    def increase_temperature(self):
        max_temperature = 30
        if self.temperature < max_temperature:
            self.temperature += 1

    def decrease_temperature(self):
        least_temperature = 16
        if self.is_on and self.temperature > least_temperature:
            self.temperature -= 1

    def toggle_on(self):
        self.is_on = not self.is_on


