"""Unit tests for the emotion detector."""

from __future__ import annotations

import unittest
from unittest.mock import MagicMock, patch

from EmotionDetection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    """Test cases for the emotion_detector function."""

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_emotion_detector_success(self, mock_post: MagicMock) -> None:
        """Verify the function returns the formatted emotion result."""

        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.text = (
            '{"emotionPredictions": [{"emotion": {'
            '"anger": 0.1, "disgust": 0.05, "fear": 0.2, '
            '"joy": 0.5, "sadness": 0.15}}]}'
        )
        mock_post.return_value = mock_response

        result = emotion_detector("I am really happy today")

        self.assertEqual(
            result,
            {
                "anger": 0.1,
                "disgust": 0.05,
                "fear": 0.2,
                "joy": 0.5,
                "sadness": 0.15,
                "dominant_emotion": "joy",
            },
        )

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_emotion_detector_400(self, mock_post: MagicMock) -> None:
        """Verify the function handles a 400 response."""

        mock_response = MagicMock()
        mock_response.status_code = 400
        mock_response.text = ""
        mock_post.return_value = mock_response

        result = emotion_detector("bad input")

        self.assertEqual(
            result,
            {
                "anger": None,
                "disgust": None,
                "fear": None,
                "joy": None,
                "sadness": None,
                "dominant_emotion": None,
            },
        )

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_emotion_detector_blank_input(self, mock_post: MagicMock) -> None:
        """Verify blank input short-circuits without calling the API."""

        result = emotion_detector("   ")

        mock_post.assert_not_called()
        self.assertEqual(
            result,
            {
                "anger": None,
                "disgust": None,
                "fear": None,
                "joy": None,
                "sadness": None,
                "dominant_emotion": None,
            },
        )


if __name__ == "__main__":
    unittest.main()
