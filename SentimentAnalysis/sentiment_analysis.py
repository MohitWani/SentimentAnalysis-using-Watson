import requests
import json

def sentiment_analyzer(text_to_analyse):
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
    header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json = myobj, headers=header)
    res = json.loads(response.text)

    if res.status_code == 200:
        label = res['documentSentiment']['label']
        score = res['documentSentiment']['score']
    elif response.status_code == 500:
        label = None
        score = None
    return {'label':label, 'score':score}