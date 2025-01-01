class Meal:
    def __init__(self, id, name, description, dt, onDiet, owner):
        self.id = id
        self.name = name
        self.description = description
        self.dt = dt
        self.onDiet = onDiet
        self.user = owner

    def __eq__(self, value):
        if not isinstance(value, Meal):
            return False
        return value.id == self.id