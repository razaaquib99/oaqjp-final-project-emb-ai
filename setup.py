"""Packaging configuration for the EmotionDetection project."""

from setuptools import find_packages, setup

setup(
    name="EmotionDetection",
    version="1.0.0",
    description="Emotion detector built with Flask and Watson NLP",
    packages=find_packages(),
    include_package_data=True,
)
