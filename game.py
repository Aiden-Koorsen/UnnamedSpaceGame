from DSEngine import *
from pygame import Vector2

if __name__ == "__main__":
    window = Window(title="Untitled Space Game", size=Vector2(1280, 720))
    while window.running:
        keys = window.frame()