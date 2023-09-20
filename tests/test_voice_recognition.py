
import unittest
import voice_recognition as vr

class TestVoiceRecognition(unittest.TestCase):

    def setUp(self):
        self.recognizer = vr.VoiceRecognizer()

    def test_recognize_voice(self):
        audio_file = 'resources/audio_samples/sample1.wav'
        expected_text = 'move mouse up'
        result = self.recognizer.recognize_voice(audio_file)
        self.assertEqual(result, expected_text)

    def test_recognize_voice_with_noise(self):
        audio_file = 'resources/audio_samples/sample2.wav'
        expected_text = 'move mouse down'
        result = self.recognizer.recognize_voice(audio_file)
        self.assertEqual(result, expected_text)

if __name__ == '__main__':
    unittest.main()
