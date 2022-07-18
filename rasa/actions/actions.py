# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions

 
from typing import Any, Text, Dict, List
import random
import requests
import wn
 
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
 
# computer_choice & determine_winner functions refactored from
# https://github.com/thedanelias/rock-paper-scissors-python/blob/master/rockpaperscissors.py, MIT liscence
 
 
class ActionPlayRPS(Action):

   
    def name(self) -> Text:
        return "action_play_rps"
 
    def computer_choice(self):
        generatednum = random.randint(1,3)
        if generatednum == 1:
            computerchoice = "rock"
        elif generatednum == 2:
            computerchoice = "paper"
        elif generatednum == 3:
            computerchoice = "scissors"
       
        return(computerchoice)
 
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
 
        # play rock paper scissors
        user_choice = tracker.get_slot("choice")
        dispatcher.utter_message(text=f"You chose {user_choice}")
        comp_choice = self.computer_choice()
        dispatcher.utter_message(text=f"The computer chose {comp_choice}")
 
        if user_choice == "rock" and comp_choice == "scissors":
            dispatcher.utter_message(text="Congrats, you won!")
        elif user_choice == "rock" and comp_choice == "paper":
            dispatcher.utter_message(text="The computer won this round.")
        elif user_choice == "paper" and comp_choice == "rock":
            dispatcher.utter_message(text="Congrats, you won!")
        elif user_choice == "paper" and comp_choice == "scissors":
            dispatcher.utter_message(text="The computer won this round.")
        elif user_choice == "scissors" and comp_choice == "paper":
            dispatcher.utter_message(text="Congrats, you won!")
        elif user_choice == "scissors" and comp_choice == "rock":
            dispatcher.utter_message(text="The computer won this round.")
        else:
            dispatcher.utter_message(text="It was a tie!")
 
        return []


class ActionResponseProduct(Action):

   
    def name(self) -> Text:
        return "action_response_product"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
 
        # producto todo con minusculas
        user_ask_product = tracker.get_slot("name_product")
        print("PRODUCTO IDENTIFICADO: ",user_ask_product)
        # user_ask_product = user_ask_product.lower()
        dispatcher.utter_message(text=f"Has preguntado por {user_ask_product}")

        # res = requests.get('https://latinwordnet.exeter.ac.uk/api/index/')
        # print(res.text)

        # es = wn.Wordnet('omw-es:1.4')
        # response = es.words(user_ask_product)[0]
        # print("PALABRA: ", response)
        # print(response)
        # print(response.pos)
        # print(response.forms())
        # print(response.lemma())
        # # print(response.derivated_words())
        # print(response.senses())
        # print(response.synsets())
        # print("------------------------------------------------")
        
        if user_ask_product == "Carne":
            dispatcher.utter_message(text="El pasillo de las Carnes es el pasillo 8")
        elif user_ask_product == "Fruta":
            dispatcher.utter_message(text="El pasillo de las frutas es el pasillo 6")
        elif user_ask_product == "Lacteo":
            dispatcher.utter_message(text="El pasillo de los Lacteos es el pasillo 3")
        elif user_ask_product == "Aseo personal":
            dispatcher.utter_message(text="El pasillo del aseo personal es el pasillo 5")
        elif user_ask_product == "Reposteria":
            dispatcher.utter_message(text="El pasillo de la repostería es el pasillo")
        elif user_ask_product == "Ropa":
            dispatcher.utter_message(text="El pasillo de la ropa es el pasillo 6")
        elif user_ask_product == "platano":
            dispatcher.utter_message(text="El platano es muy rico ñam ñam")
        else:
            dispatcher.utter_message(text="No he encontrado el producto que estas buscando")
 
        return []
   
