# Contains all the input management code for keyboards, mice and controllers
import pygame

class InputManager:
    def __init__(self):
        self.keys = None

    def update(self):
        self.keys = pygame.key.get_pressed()
        
    def isKeyDown(self, key) -> bool:
        return self.keys[key]