from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import random

class ActionShowPlayerStats(Action):
    def name(self) -> str:
        return "action_show_player_stats"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict):
        
        player = tracker.get_slot("player")
        print(f"Player name from slot: {player}")

        player_name = player
        team = "Inter Miami CF"
        stats = {
            "Matches Played": random.randint(50, 100),
            "Goals": random.randint(10, 40),
            "Assists": random.randint(5, 20),
            "Pass Accuracy": str(random.randint(70, 95)) + "%",
            "Shots on Target": random.randint(40, 50),
            "Tackles": random.randint(5, 20),
            "Minutes Played": random.randint(2000, 4000)
        }

        response = f"Hey! Here's what I found for {player_name} this season:\n\n" \
           f"🏆 Team: {team}\n" + \
           "\n".join([f"{k}: {v}" for k, v in stats.items()]) + \
           "\n\nPretty impressive, right? 😎"



        if not player:
            dispatcher.utter_message(text="Please provide a player's name.")
            return []

        # response_text = f"Fetching stats for player: {player}"
        dispatcher.utter_message(text=response)
        print("Message sent:", response)

        return []
    