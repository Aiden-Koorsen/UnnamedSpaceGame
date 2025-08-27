# Base code for an ECS that the user will call to setup an ECS for their game
class Entity:
    def __init__(self, id, name = None):
        self.id = id
        self.components = {}
        self.name = name

    def add_component(self, component):
        self.components[type(component)] = component

class EntityManager:
    def __init__(self,):
        self.next_entity_id = 0
        self.entities = []

    def create_new_entity(self, name = None) -> Entity:
        entity = Entity(self.next_entity_id, name)
        self.next_entity_id += 1
        return entity