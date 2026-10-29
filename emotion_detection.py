import requests


def emotion_detector(text_to_analyze):
    """Send text to the emotion analysis service and return its response."""

    if not isinstance(text_to_analyze, str) or not text_to_analyze.strip():
        return {"error": "Invalid or empty input"}

    # Replace this URL with the endpoint provided by your course.
    url = "YOUR_WATSON_NLP_ENDPOINT"

    response = requests.post(
        url,
        json={"raw_document": {"text": text_to_analyze}},
        timeout=30
    )

    if response.status_code == 400:
        return {"error": "Invalid input"}

    response.raise_for_status()
    return response.json()
