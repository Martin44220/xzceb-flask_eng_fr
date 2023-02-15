'''
This module is for translation service
'''
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
version = os.environ['version']

authenticator = IAMAuthenticator(f'{apikey}')
language_translator = LanguageTranslatorV3(
    version=version,
    authenticator=authenticator
)

language_translator.set_service_url(f'{url}')

language_translator.set_disable_ssl_verification(False)

def english_to_french(english_text):
    '''this function is for translating english text to french'''
    if english_text:
        return language_translator.translate(
            text=f'{english_text}',
            model_id='en-fr'
        ).get_result()['translations'][0]['translation']
    else:
        return None


def french_to_english(french_text):
    print('cer')
    '''this function is for translating the french text to english'''
    if french_text:
        return language_translator.translate(
            text=f'{french_text}',
            model_id='fr-en'
        ).get_result()['translations'][0]['translation']
    else:
        return None

print(french_to_english('Bonjour'))
print(english_to_french('Hello'))