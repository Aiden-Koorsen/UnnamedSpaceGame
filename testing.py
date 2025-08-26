# This is file for testing the new engine
import DSEngine_New as ds

if __name__ == "__main__":
    window = ds.Window()
    input = ds.InputManager()

    while window.running:
        window.handleEvents()
        input.update()

        window.beginFrame()
        
        window.endFrame()

        window.clock.tick()  # call once per frame
        fps = window.clock.get_fps()
        print(f"FPS: {fps:.2f}")

    window.shutdown()