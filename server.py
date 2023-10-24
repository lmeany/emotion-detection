'''Executing this function initiates the application of sentiment
    analysis to be execute over the Flask channel and deployed on
    localhost:5000
'''

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route('/emotionDetector')
def sent_detector():
    '''
        This code receives the text from the HTML interface and
        runs emotion detection over its using emotion_detector()
        funciton. The output returned shows the label and its confidence
        score for the provided text.
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    response_text = f"For the given statement, the emotion is 'anger': \
                    {response['anger']}, 'disgust': {response['disgust']}, \
                    'fear': {response['fear']}, 'joy': {response['joy']}, \
                    'sadness': {response['sadness']}. The dominant emotion is \
                    {response['dominant_emotion']}."
    
    if response['dominant_emotion'] is None:
        return "Invalid input! Try again!"

    return response_text

@app.route('/')
def render_index_page():
    '''
        This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
