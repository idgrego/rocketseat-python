class Meal:

    __counter = 0

    def __init__(self, name, description, dt, onDiet):
        Meal.__counter += 1
        self.id = Meal.__counter
        self.name = name
        self.description = description
        self.dt = dt
        self.onDiet = onDiet

    def __eq__(self, value):
        if not isinstance(value, Meal):
            return False
        return value.id == self.id