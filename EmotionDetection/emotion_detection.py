"""Emotion detection using the Watson NLP API."""

from __future__ import annotations

import json
from typing import Any, Dict

import requests

API_URL = (
    "https://sn-watson-emotion-lrg-lw.mybluemix.net/"
    "v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
)


def emotion_detector(text_to_analyze: str) -> Dict[str, Any]:
    """Return emotion scores and the dominant emotion for the supplied text."""

    if not text_to_analyze or not text_to_analyze.strip():
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None,
        }

    response = requests.post(API_URL, json={"text": text_to_analyze}, timeout=10)

    if response.status_code == 400:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None,
        }

    response_data = json.loads(response.text)
    emotions = response_data["emotionPredictions"][0]["emotion"]
    dominant_emotion = max(emotions, key=emotions.get)

    return {
        "anger": emotions["anger"],
        "disgust": emotions["disgust"],
        "fear": emotions["fear"],
        "joy": emotions["joy"],
        "sadness": emotions["sadness"],
        "dominant_emotion": dominant_emotion,
    }
