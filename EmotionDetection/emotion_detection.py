import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }

    try:
        response = requests.post(url, json=myobj, headers=header )
    except Exception as e:
        return {'message':'invalid input'}
    
    formatted_response = json.loads(response.text)
    emotions_stats = formatted_response['emotionPredictions'][0]['emotion']
    
    # Finding the dominant emotion
    dominant_emotion = max(emotions_stats, key= emotions_stats.get)
    
    emotions_stats['dominant_emotion'] = dominant_emotion

    if response.status_code == 400:
        for key in emotions_stats:
            emotions_stats[key] = None
        return emotions_stats

    return emotions_stats