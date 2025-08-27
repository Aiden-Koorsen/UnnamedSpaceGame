import pygame
import sys
import time

import imgui
from imgui.integrations.pygame import PygameRenderer
import OpenGL.GL as gl

# Constants
TICK_RATE = 60  # game updates per second
TICK_TIME = 1.0 / TICK_RATE  # time per update in seconds

class Window:
    def __init__(self, title="DSEngine Window", size: tuple=(1280, 720), icon=pygame.image.load("default.icon.png")):
        # Setup pygame window
        self.surface = pygame.display.set_mode(size, pygame.DOUBLEBUF | pygame.OPENGL | pygame.RESIZABLE)
        pygame.display.set_icon(icon)
        pygame.display.set_caption(title)
        
        self.clock = pygame.time.Clock()
        self.running = True

        # Frame rate independence setup
        self.last_time = time.perf_counter()
        self.accumulator = 0.0

        # Setup imgui system
        imgui.create_context()

        self.impl = PygameRenderer()
        self.io = imgui.get_io()
        self.io.display_size = self.surface.get_size()


    # Handle all window events here
    def handle_events(self):
        # Update frametiming first, so the game only updates 60 times a second
        now = time.perf_counter()
        frame_time = now - self.last_time
        self.last_time = now
        self.accumulator += frame_time

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            self.impl.process_event(event)
        
        self.impl.process_inputs()
        imgui.new_frame()

    # Call this within your games main funciton to ensure that you only update the game 60 times per second
    def can_update(self) -> bool:
        if self.accumulator >= TICK_TIME:
            self.accumulator -= TICK_TIME
            return True
        
        return False

    # Call this before drawing anything to screen
    def begin_frame(self):
        gl.glClearColor(0, 0, 0, 1)
        gl.glClear(gl.GL_COLOR_BUFFER_BIT)

    # Call this after drawing to the screen
    def end_frame(self):
        imgui.render()
        self.impl.render(imgui.get_draw_data())

        pygame.display.flip()
        self.clock.tick()

    # Handle shutdown
    def shutdown(self):
        pygame.quit()
        sys.exit()