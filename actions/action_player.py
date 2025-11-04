from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionShowPlayerStats(Action):
    def name(self) -> str:
        return "action_show_player_stats"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict):
        
        player = tracker.get_slot("player")
        print(f"Player name from slot: {player}")

        if not player:
            dispatcher.utter_message(text="Please provide a player's name.")
            return []

        response_text = f"Fetching stats for player: {player}"
        dispatcher.utter_message(text=response_text)
        print("Message sent:", response_text)

        return []
