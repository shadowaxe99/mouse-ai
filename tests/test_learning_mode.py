
import unittest
from src import learning_mode

class TestLearningMode(unittest.TestCase):

    def setUp(self):
        self.learning_mode = learning_mode.LearningMode()

    def test_record_actions(self):
        self.learning_mode.record_actions()
        self.assertIsNotNone(self.learning_mode.actions)

    def test_train_model(self):
        self.learning_mode.train_model()
        self.assertTrue(self.learning_mode.model_trained)

    def test_predict_action(self):
        action = self.learning_mode.predict_action()
        self.assertIn(action, self.learning_mode.actions)

if __name__ == '__main__':
    unittest.main()
