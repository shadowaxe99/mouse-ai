
import tensorflow as tf
from tensorflow import keras
from pyautogui import moveTo, position

class LearningMode:
    def __init__(self):
        self.model = keras.models.load_model('../models/ai_model.h5')

    def record_mouse_movement(self):
        self.mouse_positions = []
        while True:
            self.mouse_positions.append(position())
            if len(self.mouse_positions) > 1000:
                break

    def train_model(self):
        x_train = self.mouse_positions[:-1]
        y_train = self.mouse_positions[1:]
        self.model.fit(x_train, y_train, epochs=5)

    def predict_next_position(self, current_position):
        return self.model.predict(current_position)

    def move_mouse(self):
        current_position = position()
        next_position = self.predict_next_position(current_position)
        moveTo(next_position)

if __name__ == "__main__":
    learning_mode = LearningMode()
    learning_mode.record_mouse_movement()
    learning_mode.train_model()
    learning_mode.move_mouse()
