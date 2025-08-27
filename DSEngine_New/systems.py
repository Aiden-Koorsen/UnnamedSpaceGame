from .entities import EntityManager
import pygame
from .components import *
from .assets import AssetManager

# This is a number of included systems for the engine
class RenderableSystem:
    def __init__(self, em: EntityManager, screen: pygame.Surface, asset_manager: AssetManager):
        self.em = em
        self.screen = screen
        self.am = asset_manager
    
    def update(self):
        for id in self.em.entities:
            entity = self.em.entities[id]

            if entity.has_components([Renderable, Position]):
                renderable = entity.components[Renderable]
                position = entity.components[Position]
                texture = self.am.get_texture(renderable.key)

                if texture is not None:
                    self.screen.blit(texture, position.tuple_pos)