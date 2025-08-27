# Base code for an ECS that the user will call to setup an ECS for their game
class Entity:
    def __init__(self, id, name = None):
        self.id
        self.components = {}
        self.name = name

class EntityManager:
    def __init__(self,):
        self.next_entity_id = 0
        self.entities = []

    def create_new_entity():
        pass