
import voice_recognition
import mouse_control
import learning_mode

def main():
    while True:
        command = voice_recognition.listen()
        if command == "start learning":
            learning_mode.start()
        elif command == "stop learning":
            learning_mode.stop()
        elif command == "move mouse":
            mouse_control.move()
        elif command == "click":
            mouse_control.click()
        elif command == "double click":
            mouse_control.double_click()
        elif command == "right click":
            mouse_control.right_click()
        elif command == "exit":
            break

if __name__ == "__main__":
    main()
