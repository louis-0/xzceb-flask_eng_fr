import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

#authenticate
authenticator = IAMAuthenticator(apikey)

#setup service
lt = LanguageTranslatorV3(version='2018-05-01', authenticator=authenticator)
lt.set_service_url(url)
lt.set_disable_ssl_verification(True)

def englishToFrench(englishText):
    #write the code here
    frenchText = lt.translate(text=englishText, model_id='en-fr').get_result()
    return frenchText.get('translations')[0].get('translation')

def frenchToEnglish(frenchText):
    #write the code here
    englishText = lt.translate(text=frenchText, model_id='en-fr').get_result()
    return englishText.get('translations')[0].get('translation')