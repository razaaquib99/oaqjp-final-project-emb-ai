"""Unit tests for the emotion detector."""

from __future__ import annotations

from unittest.mock import MagicMock, patch

from EmotionDetection import emotion_detector


@patch("EmotionDetection.emotion_detection.requests.get")
def test_emotion_detector_success(mock_get: MagicMock) -> None:
    """Verify the function returns the formatted emotion result."""

    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.text = (
        '{"emotionPredictions": [{"emotion": {'
        '"anger": 0.1, "disgust": 0.05, "fear": 0.2, '
        '"joy": 0.5, "sadness": 0.15}}]}'
    )
    mock_get.return_value = mock_response

    result = emotion_detector("I am really happy today")

    assert result == {
        "anger": 0.1,
        "disgust": 0.05,
        "fear": 0.2,
        "joy": 0.5,
        "sadness": 0.15,
        "dominant_emotion": "joy",
    }


@patch("EmotionDetection.emotion_detection.requests.get")
def test_emotion_detector_400(mock_get: MagicMock) -> None:
    """Verify the function handles a 400 response."""

    mock_response = MagicMock()
    mock_response.status_code = 400
    mock_response.text = ""
    mock_get.return_value = mock_response

    result = emotion_detector("bad input")

    assert result == {
        "anger": None,
        "disgust": None,
        "fear": None,
        "joy": None,
        "sadness": None,
        "dominant_emotion": None,
    }


@patch("EmotionDetection.emotion_detection.requests.get")
def test_emotion_detector_blank_input(mock_get: MagicMock) -> None:
    """Verify blank input short-circuits without calling the API."""

    result = emotion_detector("   ")

    mock_get.assert_not_called()
    assert result == {
        "anger": None,
        "disgust": None,
        "fear": None,
        "joy": None,
        "sadness": None,
        "dominant_emotion": None,
    }
