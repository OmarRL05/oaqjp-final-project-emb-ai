import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }

    emotions_dict = { 'anger': None, 'disgust': None, 'fear': None, 'joy': None,'sadness': None, 'dominant_emotion': None}

    try:
        response = requests.post(url, json=myobj, headers=header )
    except Exception as e:
        return emotions_dict

    if response.status_code == 400:
        return emotions_dict

    formatted_response = json.loads(response.text)
    emotions_stats = formatted_response['emotionPredictions'][0]['emotion']

    # Finding the dominant emotion
    dominant_emotion = max(emotions_stats, key= emotions_stats.get)
    
    emotions_stats['dominant_emotion'] = dominant_emotion

    return emotions_stats