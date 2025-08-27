# This is file for testing the new engine
import DSEngine_New as ds

if __name__ == "__main__":
    window = ds.Window()
    input = ds.InputManager()
    timer = ds.Timer(1000)

    while window.running:
        window.handle_events()
        input.update()
        timer.update_timer(window.clock.get_time())

        window.begin_frame()
        
        ds.imgui.show_test_window()

        window.end_frame()

        if timer.has_elasped():
            fps = window.clock.get_fps()
            print(f"FPS: {fps:.2f}")

    window.shutdown()