"""
This provides a Flask web application for detecting emotions in text using the Watson Emotion API.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask('Emotion Detector')

@app.route("/emotionDetector")
def emot_detector():
    """
    Endpoint to analyze the emotion of the provided text.
    
    Retrieves the text to analyze from the request's query parameters,
    processes it using the emotion_detector function, and returns a 
    JSON response with the detected emotions and the dominant emotion.
    
    Returns:
        JSON: A dictionary containing the detected emotions and the dominant emotion,
              or an error message if the input text is invalid.
    """
    text_to_analyse = request.args.get('textToAnalyze', '')

    response = emotion_detector(text_to_analyse)

    if response['dominant_emotion'] is None:
        response_text = "Invalid text! Please try again."
    else:
        response_text = (
            f"For the given statement, the system response is 'anger': {response['anger']}, "
            f"'disgust':{response['disgust']}, 'fear': {response['fear']}, 'joy': {response['joy']}"
            f"and 'sadness': {response['sadness']}. The dominant emotion is "
            f"{response['dominant_emotion']}."
        )

    return response_text

@app.route('/')
def render_index_page():
    """
    Renders the index page.
    
    Returns:
        Response: The HTML content of the index page.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
