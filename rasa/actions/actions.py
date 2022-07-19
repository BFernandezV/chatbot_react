# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions

 
from typing import Any, Text, Dict, List
import random

import wn
import json
from autocorrect import Speller
from nltk.corpus import wordnet
 
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
 
# computer_choice & determine_winner functions refactored from
# https://github.com/thedanelias/rock-paper-scissors-python/blob/master/rockpaperscissors.py, MIT liscence
 

def cleanText(text):
    # print("CLEAN TEXT: ", text)
    if(text.find("?") >= 0):
        text = text.replace("?","")

    if(text.find("la ") >= 0):
        return text.replace("la ", "")
    elif(text.find("los ") >= 0):
        return text.replace("los ", "")
    elif(text.find("del ") >= 0):
        return text.replace("del ", "")
    elif(text.find("un ") >= 0):
        return text.replace("un ", "")
    elif(text.find("una ") >= 0):
        return text.replace("una ", "")
    elif(text.find("las ") >= 0):
        return text.replace("las ", "")
    elif(text.find("unos ") >= 0):
        return text.replace("unos ", "")
    elif(text.find("buscando ") >= 0):
        return text.replace("buscando ", "")
    return "Producto desconocido"


class ActionAnswerProduct(Action):
    def name(self) -> Text:
        return "action_answer_product"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
 
        # producto todo con minusculas
        account_number = tracker.get_slot("producto")
        # print("ORIGINAL:", account_number)

        if(account_number != None): 
            account_number = cleanText(account_number.lower())

        spell = Speller('es')
        word = spell(account_number)
        # print("CORRECTOR: ",word)
        # print("------------------------------------------")

        file = open('knowledge_base_data.json')
        data = json.load(file)
        categorias_encontradas = dict()

        for category in data["data"]:
            # capturar informacion
            for product in category['productos']:
                name_product = product['name']
                name_category = category['name']
                if(name_product.lower().find(word) >= 0):
                    categorias_encontradas[name_category] = category['pasillo']
            # procesar informacion
            # caso 1: los productos encontrados pertenecen a una misma categoría
                # respuesta: "nombre de categoria" y "pasillo"
        if(len(categorias_encontradas) == 1):
            for key, value in categorias_encontradas.items():
                dispatcher.utter_message(text=f"La categoría que buscas es {key}, que se encuentra en el pasillo {value}")
        elif(len(categorias_encontradas) > 1):
            dispatcher.utter_message(text=f"He encontrado las siguientes categorias: ")
            for key, value in categorias_encontradas.items():
                dispatcher.utter_message(text=f"Categoría {key}, que se encuentra en el pasillo {value}")
        else:
            dispatcher.utter_message(text=f"No he encontrado la categoria correspondiente al producto: {word}")

                

       
