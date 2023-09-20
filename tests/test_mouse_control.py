
import unittest
import pyautogui
from src import mouse_control

class TestMouseControl(unittest.TestCase):

    def setUp(self):
        self.mouse_controller = mouse_control.MouseControl()

    def test_move_mouse(self):
        initial_position = pyautogui.position()
        self.mouse_controller.move_mouse(100, 100)
        final_position = pyautogui.position()
        self.assertEqual(final_position, (initial_position[0] + 100, initial_position[1] + 100))

    def test_click_mouse(self):
        initial_position = pyautogui.position()
        self.mouse_controller.click_mouse()
        final_position = pyautogui.position()
        self.assertEqual(final_position, initial_position)

if __name__ == '__main__':
    unittest.main()
