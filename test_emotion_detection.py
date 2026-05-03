"""Unit tests for the emotion detector."""

import unittest
from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    """Test cases for emotion_detector function."""

    def test_emotion_detector_joy(self):
        """Test emotion_detector returns joy as dominant emotion."""
        result = emotion_detector("I am happy")
        self.assertEqual(result["dominant_emotion"], "joy")

    def test_emotion_detector_anger(self):
        """Test emotion_detector returns anger as dominant emotion."""
        result = emotion_detector("I am angry")
        self.assertEqual(result["dominant_emotion"], "anger")

    def test_emotion_detector_sadness(self):
        """Test emotion_detector returns sadness as dominant emotion."""
        result = emotion_detector("I am sad")
        self.assertEqual(result["dominant_emotion"], "sadness")

    def test_emotion_detector_fear(self):
        """Test emotion_detector returns fear as dominant emotion."""
        result = emotion_detector("I am scared")
        self.assertEqual(result["dominant_emotion"], "fear")

    def test_emotion_detector_disgust(self):
        """Test emotion_detector returns disgust as dominant emotion."""
        result = emotion_detector("This is disgusting")
        self.assertEqual(result["dominant_emotion"], "disgust")


if __name__ == "__main__":
    unittest.main()
