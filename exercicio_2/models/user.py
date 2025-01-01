from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, id, name, username, password):
        self.id = id
        self.name = name
        self.username = username
        self.password = password
        self.meals = []

    def __str__(self):
        return self.name
    
    def __repr__(self):
        return f'<class User; username={self.username}; id={self.id}>'

    """ 
    a classe UserMixin já possui essa definição
    é importante ou ter a propriedade 'id' ou sobreescrever o método get_id

    def __eq__(self, value):
        if not isinstance(value, User):
            return False
        return value.id == self.id 
        
    """