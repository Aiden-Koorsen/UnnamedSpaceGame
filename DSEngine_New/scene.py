# Scene management code
from .assets import AssetManager
from .systems import *
from .components import *

class Scene:
    def __init__(self, name: str):
        self.em = EntityManager()
        self.systems = []
        self.name = name

    def register_system(self, system):
        self.systems.append(system)

    def update(self):
        for system in system:
            system.update()


class SceneManager:
    def __init__(self):
        self.scenes = {}
        self.current_scene = None

    def add_scene(self, scene):
        self.scenes[scene.name] = scene

    def set_active_scene(self, scene_name):
        self.current_scene = self.scenes.get(scene_name)

    def update(self, dt):
        if self.current_scene:
            self.current_scene.update(dt)