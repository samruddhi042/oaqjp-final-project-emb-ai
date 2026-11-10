"""Basic test for the emotion detection application."""
import unittest
from emotion_detection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    """Check that the application returns a response."""

    def test_response(self):
        """The response should contain the emotion predictions."""
        result = emotion_detector("I am really mad about this")
        self.assertIn('emotionPredictions', result)


if __name__ == "__main__":
    unittest.main()
