import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    # Adding the model ID header you found
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }
    
    response = requests.post(url, json=myobj, headers=headers)
    
    # Parsing the response
    formatted_response = json.loads(response.text)
    
    # Extracting the emotion dictionary
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    
    # Task 3: Finding the dominant emotion
    # This looks at all values in the dictionary and returns the key with the highest score
    dominant_emotion = max(emotions, key=emotions.get)
    
    # Building the final output dictionary as required by the assessment
    result = {
        'anger': emotions['anger'],
        'disgust': emotions['disgust'],
        'fear': emotions['fear'],
        'joy': emotions['joy'],
        'sadness': emotions['sadness'],
        'dominant_emotion': dominant_emotion
    }
    
    return result